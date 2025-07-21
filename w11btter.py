import winreg
import os
import shutil
import subprocess
import ctypes
import psutil

# Função para definir a prioridade do processo do Valorant
def set_process_priority():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'Valorant' in proc.info['name']:
            proc.nice(psutil.REALTIME_PRIORITY_CLASS)

# Função para desabilitar serviços desnecessários
def disable_services():
    services_to_disable = [
        "WSearch",  # Windows Search
        "SysMain",   # Superfetch
        "Print Spooler",  # Serviços de impressora
        "Bluetooth Support Service"  # Se não for usar Bluetooth
    ]
    
    for service in services_to_disable:
        subprocess.run(["sc", "stop", service])
        subprocess.run(["sc", "config", service, "start=", "disabled"])

def disable_aero():
    ctypes.windll.dwmapi.DwmSetWindowAttribute(
        ctypes.windll.kernel32.GetConsoleWindow(),
        20, ctypes.byref(ctypes.c_int(0)), ctypes.sizeof(ctypes.c_int)
    )

# Função para desabilitar transparência e animações do Windows
def disable_visual_effects():
    # Desabilitar transparência
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(reg_key, "EnableTransparency", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(reg_key)

    # Desabilitar animações
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(reg_key, "MenuAnimation", 0, winreg.REG_SZ, "None")
    winreg.SetValueEx(reg_key, "UserPreferencesMask", 0, winreg.REG_BINARY, b"\x9E\x3E\x07\x80\x12\x00\x00\x00")
    winreg.CloseKey(reg_key)

# Função para desabilitar notificações e atualizações automáticas
def disable_notifications_and_updates():
    # Desabilitar atualizações automáticas (recomendado apenas temporariamente)
    subprocess.run(["sc", "config", "wuauserv", "start=", "disabled"])

    # Desabilitar notificações
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\PushNotifications", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(reg_key, "NoToastApplicationNotification", 1, winreg.REG_DWORD, 1)
    winreg.CloseKey(reg_key)

# Função para forçar o modo full-screen para o Valorant
def force_fullscreen():
    subprocess.run(["taskkill", "/IM", "Valorant.exe", "/F"])
    subprocess.run(["start", "Valorant", "/fullscreen"], shell=True)

# Função principal para aplicar as otimizações
def apply_optimizations():
    # Desativar efeitos visuais desnecessários
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(reg_key, "VisualFXSetting", 0, winreg.REG_DWORD, 2)
    winreg.CloseKey(reg_key)

    # Configurar prioridade do processo do Valorant para Tempo Real
    set_process_priority()

    # Desativar Aero (efeitos gráficos avançados)
    disable_aero()

    # Desabilitar transparência e animações do Windows
    disable_visual_effects()

    # Desabilitar serviços desnecessários
    disable_services()

    # Desabilitar notificações e atualizações automáticas
    disable_notifications_and_updates()

    # Forçar o modo full-screen para o Valorant
    force_fullscreen()

    print('Otimizações aplicadas com sucesso!')

# Executar otimizações
apply_optimizations()
