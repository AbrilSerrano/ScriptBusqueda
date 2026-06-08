INSTALACION DE SCRIPT EN UBUNTU

**1 PREPARACION DEL ENTORNO**
    
    # Instalacion de Python:

        apt update
        apt install python3-pip python3-pandas -y

    # Preparacion del Entorno

        apt install pipx -y
        pipx ensurepath

    # Instalacion de Streamlit 

        pipx install streamlit

    # Instalar Pandas dentro del entorno

        pipx inject streamlit pandas

**INSTALACION DE ARCHIVOS EN EL SISTEMA**

    #Descargar la carpeta de github descomprimir el .zip y mover los archivos

        mv /home/host/ScriptBusqueda-main /opt/

    #Cambiarle los permisos

        chown -R root:root /opt/ScriptBusqueda-main
        chmod -R 755 /opt/ScriptBusqueda-main

*Nota: corroborar el nombre de la carpeta, segun de donde haya sido descargada puede variar

**CREACION DEL DEMONIO**

    #Crear el archivo del servicio
        nano /etc/systemd/system/buscador.service

        --Copiar y Pegar lo siguiente --

[Unit]
Description=Servicio de Buscador Streamlit con PIPX
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


        #Configuracion final del demonio
            
            systemctl daemon-reload
            systemctl enable buscador.service
            systemctl start buscador.service
        
        #Chekear que el demonio este funcionando

            systemctl status buscador.service

**CONFIGURACION DE ACCESO**

entrar en el navegador a la direccion "localhost:2405" 
fijar el marcador
dejar que el usuario experimente C:


