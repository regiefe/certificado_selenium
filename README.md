# Certificação com python e Selenuim [Eduardo Mendes](https://dunossauro.github.io/curso-python-selenium/certificado.html)


### Regras da certificação.

- [x] É obrigatório o uso de Page Objects.
- [x] É obrigatório que seu projeto rode em mais de um browser.
- [x] Você pode fazer isso da maneira que achar melhor usando grid, selenium-docker ou selenoid.
- [x] Essa parte você pode documentar no seu README, caso não consiga reproduzir em código
- [x] Independente da tecnologia que escolher para automatizar os arquivos de cada funcionalidade deve estar isolados. Por exemplo:
- [x]  login.py
- [x]  cadastro.py
- [x]  todo.py
- [x]  movimentacao_de_cartoes.py


### Ambiente que foi testado.

```
MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        mint@empty 
MMm----::-://////////////oymNMd+`     ---------- 
MMd      /++                -sNMd:    OS: Linux Mint 19.1 Tessa x86_64 
MMNso/`  dMM    `.::-. .-::.` .hMN:   Host: Latitude E5410 0001 
ddddMMh  dMM   :hNMNMNhNMNMNh: `NMm   Kernel: 4.15.0-20-generic 
    NMm  dMM  .NMN/-+MMM+-/NMN` dMM   Uptime: 2 hours, 9 mins 
    NMm  dMM  -MMm  `MMM   dMM. dMM   Packages: 2543 
    NMm  dMM  -MMm  `MMM   dMM. dMM   Shell: zsh 5.4.2 
    NMm  dMM  .mmd  `mmm   yMM. dMM   Resolution: 1280x800, 1360x768 
    NMm  dMM`  ..`   ...   ydm. dMM   WM: i3 
    hMM- +MMd/-------...-:sdds  dMM   Theme: Mint-Y [GTK3] 
    -NMm- :hNMNNNmdddddddddy/`  dMM   Icons: Mint-Y [GTK3] 
     -dMNs-``-::::-------.``    dMM   Terminal: gnome-terminal 
      `/dMNmy+/:-------------:/yMMM   CPU: Intel i3 M 370 (4) @ 2.399GHz 
         ./ydNMMMMMMMMMMMMMMMMMMMMM   GPU: Intel Ironlake Mobile 
            .MMMMMMMMMMMMMMMMMMM      Memory: 1734MiB / 3744MiB 

```

 - Arquivo de configuração de hub

```
 cat hubConfig.json                                                                              
{
  "_comment" : "Configuration for Hub - hubConfig.json",
  "host": "127.0.0.1",
  "maxSession": 5,
  "port": 4444,
  "cleanupCycle": 5000,
  "timeout": 300000,
  "newSessionWaitTimeout": -1,
  "servlets": [],
  "prioritizer": null,
  "capabilityMatcher": "org.openqa.grid.internal.utils.DefaultCapabilityMatcher",
  "throwOnCapabilityNotPresent": true,
  "nodePolling": 180000,
  "platform": "LINUX"
}
```


- Ativando o ambiente Python
```
Python 3.8.2
pip 20.1.1

python -m venv .venv 
source .venv/bin/activate  
pip install -r requirements.txt
```

### Instruções de uso

Para ativar o grid tem que estar na pasta grid  e executar os dois comando a seguir.

- Para ativa o hub
```
java -jar selenium-server-standalone.jar -role hub -hubConfig hubConfig.json -debug
```

- Para ativar o node em  qualquer maquina que tenha o java e o arquivo **selenium-server-standalone.jar** 

```
java -jar selenium-server-standalone.jar -role node -hub http://localhost:4444
```

### Cadastro de usuario
```
python cadastro.py 
```
 
### Para cadastrar um todo
```
python todo.py 
```

### Para movimentar os cards
```
python movimento_de_cartoes.py
```
