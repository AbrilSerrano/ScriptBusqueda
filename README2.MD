# INSTALACION DE SCRIPT EN UBUNTU
        
## -PRIMERA FORMA-
-----------------------------------------------------------------------

### **1) PREPARACION DEL ENTORNO**
    
# Instalacion de Python:

```bash
apt update
apt install python3-pip python3-pandas -y
```

# Instalacion de pipx

```BASH
apt install pipx -y
pipx ensurepath
```

# Instalacion de Streamlit 

```BASH
pipx install streamlit
```

# Instalar Pandas dentro del entorno

```BASH
pipx inject streamlit pandas
```

### **2) INSTALACION DE ARCHIVOS EN EL SISTEMA**

#Descargar la carpeta de github descomprimir el .zip y mover los archivos

```BASH
mv /home/host/ScriptBusqueda-main /opt/
```

#Cambiarle los permisos

```BASH
chown -R root:root /opt/ScriptBusqueda-main
chmod -R 755 /opt/ScriptBusqueda-main
```

> Nota: corroborar el nombre de la carpeta, segun de donde haya sido descargada puede variar

### **3) CREACION DEL DEMONIO**

#Crear el archivo del servicio
```BASH
nano /etc/systemd/system/buscador.service
```

--Copiar y Pegar lo siguiente --

```INI
[Unit]
Description=Servicio de Buscador 
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/ScriptBusqueda-main
ExecStart=/root/.local/share/pipx/venvs/streamlit/bin/streamlit run /opt/ScriptBusqueda-main/buscador.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```


#Configuracion final del demonio
            
```BASH
systemctl daemon-reload
systemctl enable buscador.service
systemctl start buscador.service
```
        
#Chekear que el demonio este funcionando

```BASH
systemctl status buscador.service
```

### **4)CONFIGURACION DE ACCESO**

entrar en el navegador a la direccion "localhost:2405" 
fijar el marcador
dejar que el usuario experimente C:


## SEGUNDA FORMA (inicio manual)

#realizamos el paso 1, 2 de igual manera.
#el paso 3 no habilitamos el demonio para inicio automatico, es decir, omitimos:  
```BASH
systemctl enable buscador.service
```

### #4) CREAR EL LANZADOR

#creamos el lanzador en /usr/share/applications/

```BASH
nano buscador.desktop 
```

```INI
[Desktop Entry]
Version=1.0
Type=Application
Name=Buscador Inteligente
Comment=Arranca el servicio y abre el navegador
Exec=/opt/ScriptBusqueda-main/iniciar_buscador.sh
Icon=system-search
Terminal=false
Categories=Utility; 
```

#Le damos permisos

```BASH
chmod 755 buscador.desktop
```

#Lo copiamos al escritorio:

```BASH
cp buscador.desktop /home/host/Escritorio
```

# Damos permisos de visudo al usuario para ejecutar el .sh

```BASH
visudo /etc/sudoers.d/buscador
```

#Agregar la linea, remplazando usuario_comun por el host

```TEXT
usuario_comun ALL=(ALL) NOPASSWD: /usr/bin/systemctl start buscador.service
```
#Copiar el .desktop al Escritorio. Darle a permitir lanzar 

listo :)