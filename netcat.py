#Importando bibliotecas essenciais
import sys
import socket
import getopt
import threading
import subprocess

#Definindo variaveis globais
listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0