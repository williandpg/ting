<h1><strong>TING - Trybe Is Not Google</strong></h1>

<h2><strong>Descrição</strong></h2>
<p align="justify">
  Projeto que implementa um simulador de algoritmo de indexação de documentos em Python. O sistema permite anexar arquivos de texto no formato TXT e realizar buscas por termos nesses documentos, retornando em quais linhas cada palavra aparece.
  O foco está no uso de estruturas de dados lineares para organizar a leitura e a consulta dos arquivos.
</p>

<h2><strong>Funcionalidades</strong></h2>
<ul>
  <li align="justify">
    <strong>Fila de arquivos</strong>: implementação manual de uma fila FIFO para armazenar os arquivos que
    serão processados na ordem em que foram adicionados.
  </li>
  <li align="justify">
    <strong>Importação de arquivos TXT</strong>: leitura de arquivos de texto linha a linha, com validação de extensão
    e tratamento de erros quando o arquivo não é encontrado.
  </li>
  <li align="justify">
    <strong>Metadados dos documentos</strong>: exibição de informações como nome do arquivo, quantidade de linhas e
    conteúdo bruto armazenado em memória.
  </li>
  <li align="justify">
    <strong>Remoção de arquivos da fila</strong>: remoção do primeiro arquivo processado, com mensagens informativas
    sobre sucessos ou tentativas em filas vazias.
  </li>
  <li align="justify">
    <strong>Busca de palavras</strong>: função que verifica se uma palavra existe nos arquivos carregados
    e retorna em quais linhas ela aparece, de forma case insensitive.
  </li>
  <li align="justify">
    <strong>Busca detalhada</strong>: variação da busca que também retorna o conteúdo das linhas onde a
    palavra foi encontrada, facilitando a análise do contexto.
  </li>
</ul>

<h2><strong>Demonstração do Projeto</strong></h2>
<p align="center">
  <em> Projeto sem demonstração visual. Apenas linha de comando. </em>
</p>

<h2><strong>Tecnologias Utilizadas</strong></h2>
<ul>
  <li align="justify">
    <a href="https://www.python.org/" target="_blank">
      <strong>Python</strong></a>: Linguagem principal utilizada para implementar as estruturas de dados e o algoritmo de indexação de documentos.
  </li>
  <li align="justify">
    <a href="https://docs.pytest.org/" target="_blank">
      <strong>Pytest</strong></a>: Framework de testes utilizado para validar o comportamento das filas, buscas e funções de gerenciamento de arquivos.
  </li>
  <li align="justify">
    <a href="https://flake8.pycqa.org/" target="_blank">
      <strong>Flake</strong></a>: Ferramenta de linting para garantir qualidade de código e padronização de estilo em Python.
  </li>
  <li align="justify">
    <a href="https://pip.pypa.io/" target="_blank">
      <strong>pip</strong></a>: Gerenciador de pacotes para instalação de dependências, junto com ambiente virtual <code>venv</code> para isolamento do ambiente de desenvolvimento.
  </li>
</ul>

<h2><strong>Estrutura do Projeto</strong></h2>
<p align="justify">
  A estrutura do projeto é organizada da seguinte forma:
</p>
<pre><code>/
├── statics/
│   ├── arquivo_teste.txt
│   ├── novo_paradigma_globalizado.txt
│   └── novo_paradigma_globalizado-min.txt
├── tests/
│   └── __init__.py
├── ting_file_management/
│   ├── file_management.py
│   └── file_process.py
├── ting_word_searches/
│   └── word_search.py
├── dev-requirements.txt
├── requirements.txt
├── pyproject.toml
├── setup.cfg
├── setup.py
└── README.md
</code></pre>

<h2><strong>Contato</strong></h2>
<p>
  <strong>Willian Gonçalves</strong> |
  <a href="https://www.linkedin.com/in/williandpg/" target="_blank" rel="noreferrer"><strong>LinkedIn</strong></a> |
  <a href="https://github.com/williandpg" target="_blank" rel="noreferrer"><strong>Github</strong></a> |
  <a href="https://williandpg.github.io/" target="_blank" rel="noreferrer"><strong>Portfólio</strong></a> |
  <a href="mailto:goncalves.wdp@outlook.com" target="_blank" rel="noreferrer"><strong>Email</strong></a>
</p>

<h2><strong>Créditos</strong></h2>
<p align="justify">
  Projeto desenvolvido no curso de Ciência da Computação da Trybe como parte do curso de desenvolvimento full stack.
</p>

<details>
  <summary><strong>English Version</strong></summary>

  <h1><strong>TING - Trybe Is Not Google</strong></h1>

  <h2><strong>Description</strong></h2>
  <p align="justify">
    Project that implements a simple document indexing algorithm in Python. The program loads TXT files into a queue and provides search functions that return in which lines a given word appears. The main goal is to practice data structures such as queues, stacks and linked lists.
  </p>

  <h2><strong>Features</strong></h2>
  <ul>
    <li align="justify">
      <strong>File Queue</strong>: manual implementation of a FIFO queue to store files to be processed in the order they were added.
    </li>
    <li align="justify">
      <strong>TXT File Import</strong>: reading text files line by line, with extension validation and error handling when the file is not found.
    </li>
    <li align="justify">
      <strong>Document Metadata</strong>: display of information such as file name, number of lines, and raw content stored in memory.
    </li>
    <li align="justify">
      <strong>File Removal from Queue</strong>: removal of the first processed file, with informative messages about successes or attempts on empty queues.
    </li>
    <li align="justify">
      <strong>Word Search</strong>: function that checks if a word exists in the loaded files and returns in which lines it appears, case insensitive.
    </li>
    <li align="justify">
      <strong>Detailed Search</strong>: variation of the search that also returns the content of the lines where the word was found, facilitating context analysis.
    </li>
  </ul>

  <h2><strong>Project Demonstration</strong></h2>
  <p align="center">
    <em> No visual demonstration. Command line only. </em>
  </p>

  <h2><strong>Technologies Used</strong></h2>
  <ul>
    <li align="justify">
      <a href="https://www.python.org/" target="_blank">
        <strong>Python</strong></a>: Main language used to implement data structures and the document indexing algorithm.
    </li>
    <li align="justify">
      <a href="https://docs.pytest.org/" target="_blank">
        <strong>Pytest</strong></a>: Testing framework used to validate the behavior of queues, searches, and file management functions.
    </li>
    <li align="justify">
      <a href="https://flake8.pycqa.org/" target="_blank">
        <strong>Flake</strong></a>: Linting tool to ensure code quality and style standardization in Python.
    </li>
    <li align="justify">
      <a href="https://pip.pypa.io/" target="_blank">
        <strong>pip</strong></a>: Package manager for installing dependencies, along with the <code>venv</code> virtual environment for development environment isolation.
    </li>
  </ul>

  <h2><strong>Project Structure</strong></h2>
  <p align="justify">
    The project structure is organized as follows:
  </p>
  <pre><code>/
  ├── statics/
  │   ├── arquivo_teste.txt
  │   ├── novo_paradigma_globalizado.txt
  │   └── novo_paradigma_globalizado-min.txt
  ├── tests/
  │   └── __init__.py
  ├── ting_file_management/
  │   ├── file_management.py
  │   └── file_process.py
  ├── ting_word_searches/
  │   └── word_search.py
  ├── dev-requirements.txt
  ├── requirements.txt
  ├── pyproject.toml
  ├── setup.cfg
  ├── setup.py
  └── README.md
  </code></pre>

  <h2><strong>Contact</strong></h2>
  <p>
    <strong>Willian Gonçalves</strong> |
    <a href="https://www.linkedin.com/in/williandpg/" target="_blank" rel="noreferrer"><strong>LinkedIn</strong></a> |
    <a href="https://github.com/williandpg" target="_blank" rel="noreferrer"><strong>Github</strong></a> |
    <a href="https://williandpg.github.io/" target="_blank" rel="noreferrer"><strong>Portfolio</strong></a> |
    <a href="mailto:goncalves.wdp@outlook.com" target="_blank" rel="noreferrer"><strong>Email</strong></a>
</p>

  <h2><strong>Credits</strong></h2>
  <p align="justify">
    Project developed at Trybe as part of the Computer Science curriculum.
  </p>
</details>