# Python Terminal - Drácula

Esta aplicação é uma implementação de um terminal Python personalizado com estilo Drácula, utilizando a biblioteca PyQt5 e o módulo qtconsole. A aplicação consiste em uma janela principal (QMainWindow) que contém um widget personalizado chamado PythonTerminal.

O PythonTerminal é um QWidget que cria e gerencia um console Python interativo (RichJupyterWidget). Ele utiliza um gerenciador de kernel (QtInProcessKernelManager) para gerenciar a comunicação entre o console e o kernel Python. O console é personalizado com um estilo Drácula e captura eventos de teclado para detectar quando a tecla Enter é pressionada.

## Imagem da aplicação:
![image](https://user-images.githubusercontent.com/101942554/226219786-6376ba7c-0e48-4503-8acc-be37ced1ac71.png)

## Bibliotecas:
sys (biblioteca padrão do Python) </br>
os (biblioteca padrão do Python) </br>
PyQt5.QtWidgets </br>
PyQt5.QtCore </br>
qtconsole.rich_jupyter_widget </br>
qtconsole.inprocess </br>

As bibliotecas PyQt5 e qtconsole não fazem parte das bibliotecas padrão do Python e precisam ser instaladas separadamente. Você pode instalá-las usando o pip: </br></br>

<pre>
pip install PyQt5 qtconsole
</pre>
