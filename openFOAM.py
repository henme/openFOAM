#!/usr/bin/python
'''
GUI for openFOAM

This program launches a guided user interface for openFOAM
So far, only incompressible flow is implemented

Requirements: openFOAM 2.2.2 with paraFOAM running on UBUNTU 
Made by: Henrik Kaald Melb\o
NTNU, Trondheim, Norway
Department Of Chemical Engineering
Contact: henrikkaald@gmail.com
Version: 1.0
Date: 20. Jan. 2014
'''
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from UI import Ui_openFOAM
import sys, os, time, subprocess, re, shutil
from tempfile import mkstemp
from shutil import move
from os import remove, close

###################################################
#Initiating Main GUI                              #
###################################################
class Main(QDialog, Ui_openFOAM):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Connect up the buttons and comboboxes
        self.pushButton.clicked.connect(self.selectFile) #Load mesh button
        self.pushButton_3.clicked.connect(self.load) #Load case button        
        self.pushButton_2.clicked.connect(self.new) #New case button
        self.pushButton_5.clicked.connect(self.fvSc) #Edit fvSchemes 
        self.pushButton_6.clicked.connect(self.terminal) #Terminal command
        self.pushButton_4.setEnabled(False)
        self.textEdit.setEnabled(False)
        self.label_14.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        self.pushButton_4.clicked.connect(self.para)
        self.connect(self.comboBox, QtCore.SIGNAL('activated(QString)'), self.combo) # Solvers
        applyButton = self.buttonBox.button(QtGui.QDialogButtonBox.Apply)
        QtCore.QObject.connect(applyButton, QtCore.SIGNAL("clicked()"), self.accept)
        cancelButton = self.buttonBox.button(QtGui.QDialogButtonBox.Cancel)
        self.checkBox_2.stateChanged.connect(self.nomesh)
        self.textEdit_9.setReadOnly(True)
        self.textEdit_11.setReadOnly(True)
        self.checkBox.stateChanged.connect(self.turbulence) #Turbulence
        self.Schemes.setTabEnabled(6, 0)

    #If turbulence is activated, get properties
    def turbulence(self, state):
        if state == QtCore.Qt.Unchecked:
            try:
                case
            except:
                self.textEdit.setEnabled(False)
                self.label_14.setEnabled(False)
                self.comboBox_4.setEnabled(False)
                self.Schemes.removeTab(7)
                self.turb = False
                return
            self.noturbulence()
            self.turb = False
            return 
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            self.checkBox.setCheckState(QtCore.Qt.Unchecked)
            return
        if state == QtCore.Qt.Checked:
            self.initturbulence()
            self.turb = True
            self.textEdit.setEnabled(True)
            self.label_14.setEnabled(True)
            self.comboBox_4.setEnabled(True)

    #Setup the turbulence tab
    def initturbulence(self):
        shutil.copy2(case+"/templates/k", case+"/templates/k_tmp")
        shutil.copy2(case+"/templates/epsilon", case+"/templates/epsilon_tmp")
        shutil.copy2(case+"/templates/nut", case+"/templates/nut_tmp")
        shutil.copy2(case+"/templates/nuTilda", case+"/templates/nuTilda_tmp")
        shutil.copy2(case+"/templates/turbulenceProperties", case+"/constant/turbulenceProperties")
        bound = case+"/constant/polyMesh/boundary"
        f = open(bound, 'r+')
        lines = f.readlines()
        f.close()
        num = int(lines[17])
        first = []
        for i in range(1, num+1):
            j = 13+6*i
            first.append(lines[j][:-1])
        k = case+"/templates/k_tmp"
        epsilon = case+"/templates/epsilon_tmp"
        nut = case+"/templates/nut_tmp"
        nuTilda = case+"/templates/nuTilda_tmp"
        global tcon
        tcon = len(first)
        for i in range(0, tcon):
            pb = first[i]+"\n    {\n        type            typ"+str(i)+"/*type*/;\n        value           val"+str(i)+"/*val*/; \n    }"
            self.replace(k, "/*"+str(i+1)+"*/", pb)
            self.replace(epsilon, "/*"+str(i+1)+"*/", pb)
            self.replace(nut, "/*"+str(i+1)+"*/", pb)
            self.replace(nuTilda, "/*"+str(i+1)+"*/", pb)            
        #Need to add options in tab
        i = 0
        p = 10
        #newtab = QWidget()
        #newtab_layout = QtGui.QVBoxLayout(newtab)
        newtab_2 = QtGui.QScrollArea()
        newtab_2.setWidget(QtGui.QWidget())
        newtab_layout = QtGui.QVBoxLayout(newtab_2.widget())
        newtab_2.setWidgetResizable(True)
        global tedit, tredit, t2edit, t2redit
        tedit = {}
        tredit = {}
        t2edit = {}
        t2redit = {}   
        #Auto completer
        c = QtGui.QCompleter(["fixedValue", "zeroGradient"])
        c.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        d = QtGui.QCompleter(['uniform (x y z)', 'uniform p'])
        d.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)        
        #grid positioner
        grid = QtGui.QGridLayout()
        j = 1
        lablep = QtGui.QLabel("k")
        lableu = QtGui.QLabel("epsilon")
        lablen = QtGui.QLabel("nut")
        lablem = QtGui.QLabel("nuTilda")
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setBold(True)
        lableu.setFont(font)
        lablep.setFont(font)
        lablen.setFont(font)
        lablem.setFont(font)
        grid.addWidget(lablep,0,1)
        grid.addWidget(lableu,0,2)
        grid.addWidget(lablen,0,3)
        grid.addWidget(lablem,0,4)
        font.setUnderline(False)
        while len(first) > 0:
            i += 2
            p += 1
            label = QtGui.QLabel(first.pop())
            label.setFont(font)
            grid.addWidget(label, j, 0)
            label = QtGui.QLabel("Type: ")
            grid.addWidget(label, j+1, 0)
            label = QtGui.QLabel("Value: ")
            grid.addWidget(label, j+2, 0)
            tedit[(i)] = QtGui.QComboBox()
            grid.addWidget(tedit[(i)], j+1, 1)
            tedit[(p)] = QtGui.QComboBox()
            grid.addWidget(tedit[(p)], j+2, 1)
            tredit[(i)] = QtGui.QComboBox()
            grid.addWidget(tredit[(i)], j+1, 2)
            tredit[(p)] = QtGui.QComboBox()
            grid.addWidget(tredit[(p)], j+2, 2)
            t2edit[(i)] = QtGui.QComboBox()
            grid.addWidget(t2edit[(i)], j+1, 3)
            t2edit[(p)] = QtGui.QComboBox()
            grid.addWidget(t2edit[(p)], j+2, 3)
            t2redit[(i)] = QtGui.QComboBox()
            grid.addWidget(t2redit[(i)], j+1, 4)
            t2redit[(p)] = QtGui.QComboBox()
            grid.addWidget(t2redit[(p)], j+2, 4)
            tedit[(i)].setEditable(True)
            tedit[(p)].setEditable(True)
            tredit[(i)].setEditable(True)
            tredit[(p)].setEditable(True)
            t2edit[(i)].setEditable(True)
            t2edit[(p)].setEditable(True)
            t2redit[(i)].setEditable(True)
            t2redit[(p)].setEditable(True)
            tedit[(i)].setCompleter(c)
            tedit[(p)].setCompleter(d)
            tredit[(i)].setCompleter(c)
            tredit[(p)].setCompleter(d)
            t2edit[(i)].setCompleter(c)
            t2edit[(p)].setCompleter(d)
            t2redit[(i)].setCompleter(c)
            t2redit[(p)].setCompleter(d)
            j += 3
        newtab_2.setLayout(grid)
        #Create a new tab, then switch
        self.Schemes.addTab(newtab_2, "Turbulence Properties")

    #Set the options nedded for turbulence
    def setturbulence(self):
        ras = case+"/constant/RASProperties"
        self.replace(ras, "laminar;", str(self.comboBox_4.currentText())+";")
        self.replace(ras, "off;", "on;") 
        tur = case+"/constant/turbulenceProperties"
        self.replace(tur, "nu;", self.textEdit.toPlainText()+";")
        shutil.copy2(case+"/templates/k_tmp", case+"/0/k")
        shutil.copy2(case+"/templates/epsilon_tmp", case+"/0/epsilon")
        shutil.copy2(case+"/templates/nut_tmp", case+"/0/nut")
        shutil.copy2(case+"/templates/nuTilda_tmp", case+"/0/nuTilda")
        k = case+"/0/k"
        epsilon = case+"/0/epsilon"
        nut = case+"/0/nut"
        nuTilda = case+"/0/nuTilda"
        p = 10
        i = 0
        for j in range(0, tcon):
            p += 1
            i += 2
            typ1 = tedit[(i)].currentText()
            val1 = tedit[(p)].currentText()
            typ2 = tredit[(i)].currentText()
            val2 = tredit[(p)].currentText()
            typ3 = t2edit[(i)].currentText()
            val3 = t2edit[(p)].currentText()
            typ4 = t2redit[(i)].currentText()
            val4 = t2redit[(p)].currentText()
            self.replace(k, "typ"+str(j)+"/*type*/;", str(typ1)+";")
            if typ1 == "zeroGradient":
                self.replace(k, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(k, "val"+str(j)+"/*val*/;", str(val1)+";")
            self.replace(epsilon, "typ"+str(j)+"/*type*/;", str(typ2)+";")
            if typ2 == "zeroGradient":
                self.replace(epsilon, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(epsilon, "val"+str(j)+"/*val*/;", str(val2)+";")
            self.replace(nut, "typ"+str(j)+"/*type*/;", str(typ3)+";")
            if typ3 == "zeroGradient":
                self.replace(nut, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(nut, "val"+str(j)+"/*val*/;", str(val3)+";")
            self.replace(nuTilda, "typ"+str(j)+"/*type*/;", str(typ4)+";")
            if typ4 == "zeroGradient":
                self.replace(nuTilda, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(nuTilda, "val"+str(j)+"/*val*/;", str(val4)+";")

    #Remove turbulence related files and tabs
    def noturbulence(self):
        self.textEdit.setEnabled(False)
        self.label_14.setEnabled(False)
        self.comboBox_4.setEnabled(False)
        shutil.copy2(case+"/templates/RASProperties", case+"/constant/RASProperties")
        self.Schemes.removeTab(7)

        #Do additional terminal commands

    #Allows for additional terminal commands
    def terminal(self):
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            return
        command = str(self.lineEdit_2.text())
        command = command.split(' ')
        self.lineEdit_2.clear()
        cmd = open("terminal","w")
        if len(command) == 1:
            t = subprocess.Popen([command[0]], cwd=case, stdout = cmd, stderr = cmd)
        elif len(command) == 2:
            t = subprocess.Popen([command[0], command[1]], cwd=case, stdout = cmd, stderr = cmd)
        elif len(command) == 3:
            t = subprocess.Popen([command[0], command[1], command[2]], cwd=case, stdout = cmd, stderr = cmd)
        else:
            self.textEdit_9.append("Command not recognized")            
        try:
            t
        except:
            return
        t.wait()
        cmd.close()
        self.textEdit_9.append(open(pwd+"/terminal").read())

    #Launches paraFOAM
    def para(self):
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            return
        e = subprocess.Popen(["paraFoam"], cwd = case)

    #Changes the mesh state 
    def nomesh(self, state):
        if state == QtCore.Qt.Checked:
            self.meshState = True

    #Allows for manual input in fvSchemes
    def fvSc(self):
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            return
        T = TextEdit()
        T.exec_()

        #Find and replace function

    #Function for file editing    
    def replace(self, file_path, pattern, subst):
        #Create temp file
        fh, abs_path = mkstemp()
        new_file = open(abs_path,'w')
        old_file = open(file_path)
        for line in old_file:
            new_file.write(line.replace(pattern, subst))
        #close temp file
        new_file.close()
        close(fh)
        old_file.close()
        #Remove original file
        remove(file_path)
        #Move new file
        move(abs_path, file_path)

    #Creates a new case
    def new(self):
        global case
        global pwd
        case = QFileDialog.getSaveFileName(self, "New case")
        case = str(case)
        if not case:
            del case
            return
        pwd = os.path.dirname(os.path.realpath(__file__))
        case = str(case)
        os.system("cp -r "+pwd+"/root "+case)
        self.pushButton_4.setEnabled(True)

    #Loads in a case
    def load(self):
        global case
        global pwd
        case = QFileDialog.getExistingDirectory()
        if not case:
            del case
            return
        case = str(case)
        pwd = os.path.dirname(os.path.realpath(__file__))
        os.system("cp -r "+pwd+"/root/templates "+case)
        #shutil.copy2(pwd+"/root/templates/p", case)
        #shutil.copy2(pwd+"/root/templates/U", case)
        #shutil.copy2(pwd+"/root/templates/fvSolution", case)
        #shutil.copy2(pwd+"/root/templates/controlDict", case)
        if os.path.isdir(case+"/constant/polyMesh"):
            self.findBound()
        self.pushButton_4.setEnabled(True)

    #Get program name from combobox
    def combo(self, text): #Run
        global program
        program = text
        program = str(program)
        if program == "simpleFoam":
            self.textEdit_11.setText("SimpleFoam is a steady-state solver for incompressible, turbulent flow")
        elif program == "None":
            self.textEdit_11.setText("No solver is defined")
        elif program == "icoFoam":
            self.textEdit_11.setText("icoFoam is a transient solver for incompressible, laminar flow of Newtonian fluids")
        elif program == "nonNewtonianIcoFoam":
            self.textEdit_11.setText("nonNewtonianIcoFoam is a transient solver for incompressible, laminar flow of non-Newtonian fluids")
        elif program == "pisoFoam":
            self.textEdit_11.setText("pisoFoam is a transient solver for incompressible flow")
        elif program == "pimpleFoam":
            self.textEdit_11.setText("Large time-step transient solver for incompressible, flow using the PIMPLE (merged PISO-SIMPLE) algorithm")

    #Setting the viscosity
    def visc(self):
        shutil.copy2(case+"/templates/transportProperties", case+"/constant/transportProperties")
        vis = case+"/constant/transportProperties"
        self.replace(vis, "nu;", self.textEdit_10.toPlainText()+";")

    #Checks if input is a float/number 
    def validate(self):
        if not self.isFloat(self.textEdit.toPlainText(), "Viscosity is ill defined"):
            return False
        if not self.isFloat(self.textEdit_2.toPlainText(), "Pressure tolerace is ill defined"):
            return False
        if not self.isFloat(self.textEdit_3.toPlainText(), "Velocity  tolerace is ill defined"):
            return False
        if not self.isFloat(self.textEdit_4.toPlainText(), "Lenght of simulation is ill defined"):
            return False
        if not self.isFloat(self.textEdit_5.toPlainText(), "Timestep  is ill defined"):
            return False
        if not self.isFloat(self.textEdit_6.toPlainText(), "Write interval  is ill defined"):
            return False
        if not self.isFloat(self.textEdit_7.toPlainText(), "Pressure relTol is ill defined"):
            return False
        if not self.isFloat(self.textEdit_8.toPlainText(), "Velocity relTol is ill defined"):
            return False
        return True

    #Initializing the final preparations for running the solver
    #Remaining checks and finializations
    def accept(self):
        #Read, search and replace parameters
        global delta
        global write
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            return
        if not self.validate():
            return
        try:
            program
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No solver defined", QtGui.QMessageBox.Ok)
            return
        if program == "None":
            QtGui.QMessageBox.question(self, 'An error has occured', "No solver defined", QtGui.QMessageBox.Ok)
            return
        if not os.path.isdir(case+"/constant/polyMesh"):
            QtGui.QMessageBox.question(self, 'An error has occured', "No mesh defined", QtGui.QMessageBox.Ok)
            return
        if not self.condType():
            QtGui.QMessageBox.question(self, 'An error has occured', "Ill defined boundary type", QtGui.QMessageBox.Ok)
            return
        #Want to clear out old data files
        filelist = [ f for f in os.listdir(case) if not f in ["0", "constant", "system", "T", "U", "p", "fvSolution", "templates"]]
        for f in filelist:
            if os.path.isdir(case+"/"+f):
                shutil.rmtree(case+"/"+f)
        #If turbulence
        try:
            self.turb
        except:
            self.turb = False
        if self.turb == True:
            self.setturbulence()
        #Set viscosity
        self.visc()
        #Get controlDict
        self.control()
        #Set the fvSolutions       
        self.solutions()
        #Makes boundries reversable
        shutil.copy2(case+"/templates/p_tmp", case+"/0/p")
        shutil.copy2(case+"/templates/U_tmp", case+"/0/U")
        #shutil.copy2(case+"/templates/T_tmp", case+"/0/T")
        #Check and set boundaries
        self.cond()
        #Set solver
        global p
        fh = open("Output","w")
        p = subprocess.Popen([program], cwd=case, stdout = fh, stderr = fh)
        fh.close()
        load = Loader()
        if load.Run() == 1:
            w = View()
            w.exec_()

    #Loads in mesh
    def selectFile(self): # Load and run mesh
        try:
            self.meshstate
        except:
            self.meshState = False
        if self.meshState == True:
            return
        global mesh
        global path
        try:
            case
        except:
            QtGui.QMessageBox.question(self, 'An error has occured', "No case defined", QtGui.QMessageBox.Ok)
            return
        path = QFileDialog.getOpenFileName(self, "Load Mesh", case , "*.unv *.ans *.msh *.neu *.geo")
        if not path:
            self.lineEdit.setText("Mesh")
            del path
            return
        self.lineEdit.setText(path)
        path = str(path)
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        #Copy boundarys
        suf = path.rsplit('.',1)
        os.system("cp " + path +" "+ case)
        mesh = path.rsplit('/',1)
        self.defBound(mesh, suf)
        QApplication.restoreOverrideCursor()
        self.findBound()
        #Create mesh, write info to "MehsInfo"

    #Checks whats kind of mesh is supplied, and does the necessary conversion
    def defBound(self, mesh, suf):
        gr = open("MeshInfo","w")
        if suf[-1] == "unv":
            d = subprocess.Popen(["ideasUnvToFoam", mesh[1]], cwd=case, stdout = gr, stderr = gr)
        elif suf[-1] == "neu":
            d = subprocess.Popen(["gambitToFoam", mesh[1]], cwd=case, stdout = gr, stderr = gr)
        elif suf[-1] == "msh":
            d = subprocess.Popen(["fluentMeshToFoam", mesh[1]], cwd=case, stdout = gr, stderr = gr)
        elif suf[-1] == "geo":
            d = subprocess.Popen(["cfx4ToFoam", mesh[1]], cwd=case, stdout = gr, stderr = gr)
        elif suf[-1] == "ans":
            d = subprocess.Popen(["ideasToFoam", mesh[1]], cwd=case, stdout = gr, stderr = gr)
        d.wait()
        gr.close()

    #Sets the control in ControlDict
    def control(self):
        global run, delta, write 
        cd = case+"/system/controlDict"
        run = self.textEdit_4.toPlainText()
        run = str(run)
        delta = self.textEdit_5.toPlainText()
        delta = str(delta)
        write = self.textEdit_6.toPlainText()
        write = str(write)
        shutil.copy2(case+"/templates/controlDict", case+"/system/controlDict")
        self.replace(cd, "TIMEEND", run)
        self.replace(cd, "TDELTA", delta)
        self.replace(cd, "INTERVALWRITE", write)

        # Need to find Boundaries

    #Finds the boundaries from mesh
    def findBound(self):
        shutil.copy2(case+"/templates/p", case+"/templates/p_tmp")
        shutil.copy2(case+"/templates/U", case+"/templates/U_tmp")
        #shutil.copy2(case+"/templates/T", case+"/templates/T_tmp")
        bound = case+"/constant/polyMesh/boundary"
        f = open(bound, 'r+')
        lines = f.readlines()
        f.close()
        num = int(lines[17])
        first = []
        for i in range(1, num+1):
            j = 13+6*i
            first.append(lines[j][:-1])
        #Create boundaries in U,P,T etc
        P = case+"/templates/p_tmp"
        U = case+"/templates/U_tmp"
        #T = case+"/templates/T_tmp"
        global con 
        con = len(first)
        for i in range(0, con):
            pb = first[i]+"\n    {\n        type            typ"+str(i)+"/*type*/;\n        value           val"+str(i)+"/*val*/; \n    }"
            self.replace(P, "/*"+str(i+1)+"*/", pb)
            self.replace(U, "/*"+str(i+1)+"*/", pb)
            #self.replace(T, "/*"+str(i+1)+"*/", pb)
        #Add bounadries tab
        #Need to add options in tab
        i = 0
        p = 10
        #newtab = QWidget()
        #newtab_layout = QtGui.QVBoxLayout(newtab)
        newtab = QtGui.QScrollArea()
        newtab.setWidget(QtGui.QWidget())
        newtab_layout = QtGui.QVBoxLayout(newtab.widget())
        newtab.setWidgetResizable(True)
        global edit, redit
        edit = {}
        redit = {}   
        #Auto completer
        c = QtGui.QCompleter(["fixedValue", "zeroGradient"])
        c.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        d = QtGui.QCompleter(['uniform (x y z)', 'uniform p'])
        d.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)        
        #grid positioner
        grid = QtGui.QGridLayout()
        j = 1
        lablep = QtGui.QLabel("Pressure")
        lableu = QtGui.QLabel("Velocity")
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setBold(True)
        lableu.setFont(font)
        lablep.setFont(font)
        grid.addWidget(lablep,0,1)
        grid.addWidget(lableu,0,2)
        font.setUnderline(False)
        while len(first) > 0:
            i += 2
            p += 1
            label = QtGui.QLabel(first.pop())
            label.setFont(font)
            grid.addWidget(label, j, 0)
            label = QtGui.QLabel("Type: ")
            grid.addWidget(label, j+1, 0)
            label = QtGui.QLabel("Value: ")
            grid.addWidget(label, j+2, 0)
            edit[(i)] = QtGui.QComboBox()
            grid.addWidget(edit[(i)], j+1, 1)
            edit[(p)] = QtGui.QComboBox()
            grid.addWidget(edit[(p)], j+2, 1)
            redit[(i)] = QtGui.QComboBox()
            grid.addWidget(redit[(i)], j+1, 2)
            redit[(p)] = QtGui.QComboBox()
            grid.addWidget(redit[(p)], j+2, 2)
            edit[(i)].setEditable(True)
            edit[(p)].setEditable(True)
            redit[(i)].setEditable(True)
            redit[(p)].setEditable(True)
            edit[(i)].setCompleter(c)
            edit[(p)].setCompleter(d)
            redit[(i)].setCompleter(c)
            redit[(p)].setCompleter(d)
            j += 3
        newtab.setLayout(grid)
        #Create a new tab, then switch
        self.Schemes.addTab(newtab, "Boundary Conditions")
        self.Schemes.removeTab(6)

    #Checks if float
    def isFloat(self, inp, text):
        try: 
            float(inp)
            return True
        except ValueError:
            QtGui.QMessageBox.question(self, 'An error has occured', text, QtGui.QMessageBox.Ok)
            return False

    # Set fvSolution
    def solutions(self):
        psolver = str(self.comboBox_5.currentText()) #P solver
        pprecon = str(self.comboBox_6.currentText()) #P precon
        psmooth = str(self.comboBox_7.currentText()) #P smooth
        usolver = str(self.comboBox_8.currentText()) #U solver
        uprecon = str(self.comboBox_9.currentText()) #U precon
        usmooth = str(self.comboBox_10.currentText()) #U smooth
        ptol = self.textEdit_2.toPlainText() #P tol
        utol = self.textEdit_3.toPlainText() #u tol
        preltol = self.textEdit_7.toPlainText() #P reltol
        ureltol = self.textEdit_8.toPlainText() #U reltol
        shutil.copy2(case+"/templates/fvSolution", case+"/system/fvSolution")
        sol = case+"/system/fvSolution"
        self.replace(sol, "psolver;", psolver+";")
        self.replace(sol, "pprecon;", pprecon+";")
        self.replace(sol, "psmooth;", psmooth+";")
        self.replace(sol, "usolver;", usolver+";")
        self.replace(sol, "uprecon;", uprecon+";")
        self.replace(sol, "usmooth;", usmooth+";")
        self.replace(sol, "ptol;", ptol+";")
        self.replace(sol, "utol;", utol+";")
        self.replace(sol, "preltol;", preltol+";")
        self.replace(sol, "ureltol;", ureltol+";")

    #Finds the boundary conditions (groups from geometry)
    def cond(self): 
        p = case+"/0/p"
        U = case+"/0/U"
        k = 10
        i = 0
        for j in range(0, con):
            k += 1
            i += 2
            typ1 = edit[(i)].currentText()
            val1 = edit[(k)].currentText()
            typ2 = redit[(i)].currentText()
            val2 = redit[(k)].currentText()
            self.replace(p, "typ"+str(j)+"/*type*/;", str(typ1)+";")
            if typ1 == "zeroGradient":
                self.replace(p, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(p, "val"+str(j)+"/*val*/;", str(val1)+";")
            self.replace(U, "typ"+str(j)+"/*type*/;", str(typ2)+";")
            if typ2 == "zeroGradient":
                self.replace(U, "value           val"+str(j)+"/*val*/;", "")
            else:            
                self.replace(U, "val"+str(j)+"/*val*/;", str(val2)+";")

    #Checks if leagal boundary condition type is given
    def condType(self):
        text = set()
        i = 0
        for j in range(0, con):
            i += 2
            ty1 = edit[(i)].currentText()
            ty1 = str(ty1)
            ty2 = redit[(i)].currentText()
            ty2 = str(ty2)
            text.add(ty1)
            text.add(ty2)
        values = set(["fixedValue", "fixedGradient", "zeroGradient", "calculated", "mixed", "directionMixed",
                    "movingWallVelocity", "pressureInletVelocity", "pressureDirectedInletVelocity",
                    "surfaceNormalFixedValue", "totalPressure", "turbulentInlet", "fluxCorrectedVelocity",
                    "buoyantPressure", "inletOutlet", "outletInlet", "pressureInletOutletVelocity",
                    "pressureDirectedInletOutletVelocity", "pressureTransmissive", "supersonicFreeStream",
                    "slip", "partialSlip", "patch", "empty", "symmetryPlane", "wedge", "cyclic",
                    "wall", "processor"])
        if text.issubset(values):
                return True
        else:                
                return False


###################################################
#Loadbar: While program is running                #
###################################################
class Loader(QtGui.QDialog):
    def __init__(self):
        super(Loader, self).__init__()
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.setGeometry(800, 430, 280, 150)
        self.btn = QtGui.QPushButton('Cancel', self)
        self.btn.move(80, 80)
        self.btn.clicked.connect(self.doAction)
        self.step = 0
        self.setWindowTitle('Running')
        #setup timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.completed = False
        self.term = False 

    def Run(self):
        self.timer.start(100)
        return self.exec_()

    def Complete(self, completed):
        if self.completed:
            return
        self.completed = True
        self.timer.stop()
        if p.poll() == None:
            p.kill()
            completed = False
        if completed:
            self.accept()
        else:
            self.reject()

    def Time(self):
        run2 = re.findall("\d+.\d+|\d+", run)
        delta2 = re.findall("\d+.\d+|\d+", delta)
        write2 = re.findall("\d+.\d+|\d+", write)
        run3 = float(run2.pop())
        delta3 = float(delta2.pop())
        write3 = float(write2.pop())
        tot = run3/delta3/write3
        #Counts the number of folders in case folder
        x = subprocess.Popen("ls -d */", bufsize = 1, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = case, shell = True)
        count = 0
        #Gives a % of completed "folders"
        if x.stdout:
            for line in x.stdout:
                count += 1
        if count == 4:
            self.step = 0
        else:
            self.step = (float(count-4)/tot)*100
        self.pbar.setValue(self.step)
        QtGui.qApp.processEvents()
        if p.poll() is not None:
            self.Complete(True)
        if self.term == True:
            p.kill()
            self.Complete(False)

    def doAction(self):
        #Kills the process if cancel is pressed
        self.term = True
        p.kill()
        self.deleteLater()


###################################################
#Show Output: After program is done               #
###################################################
class View(QtGui.QDialog):
    def __init__(self):
        super(View, self).__init__()
        self.setGeometry(0,0,900,600)
        self.setFixedSize(900, 600)
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(QtCore.QRect(0, 20, 900, 540))
        text = open(pwd+'/Output').read()
        self.text_edit.setText(text)
        self.setWindowTitle('Output')
        self.close = QtGui.QPushButton('Close', self)
        self.close.move(250, 565)
        self.close.clicked.connect(self.Close)
        self.save = QtGui.QPushButton('Save', self)
        self.save.move(350, 565)
        self.save.clicked.connect(self.Save)
        self.btn2 = QtGui.QPushButton('paraFOAM', self)
        self.btn2.move(450, 565)
        self.btn2.clicked.connect(self.para) 

    def Close(self):
        self.deleteLater()

    def Save(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text_edit.toPlainText()
        f.write(filedata)
        f.close()

    def para(self):
        #opens paraFoam on completion
        e = subprocess.Popen(["paraFoam"], cwd = case)


###################################################
#TextEditor for manual edit of fvSchemes          #
###################################################
class TextEdit(QtGui.QDialog):

    def __init__(self):
        super(TextEdit, self).__init__()
        self.Ui()

    def Ui(self):

        self.text_edit = QTextEdit(self)
        self.setGeometry(0,0,900,600)
        self.setFixedSize(900, 600)
        self.setWindowTitle('fvSchemes')
        self.text_edit.setGeometry(QtCore.QRect(0, 20, 900, 540))
        text = open(case+"/system/fvSchemes").read()
        self.text_edit.setText(text)
        self.close = QtGui.QPushButton('Close', self)
        self.close.move(350, 565)
        self.close.clicked.connect(self.Close)

    def Close(self):
        self.saveFile()
        self.deleteLater()

    def saveFile(self):
       f = open(case+"/system/fvSchemes", 'w')
       filedata = self.text_edit.toPlainText()
       f.write(filedata)
       f.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
