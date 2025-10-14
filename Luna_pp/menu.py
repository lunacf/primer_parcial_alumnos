import os
import keyboard
import time
import sys
import colorama
colorama.init()

def limpiar_lineas_terminal(n: int):
    """
    Limpia n lineas hacia arriba en la terminal
    """
    for _ in range(n):
        sys.stdout.write('\033[1A')  # Mover cursor arriba
        sys.stdout.write('\033[2K')  # Limpiar línea completa
    sys.stdout.flush()

def limpiar_buffer_entrada():
    """Limpia el buffer de entrada del teclado"""
    if os.name == 'nt':  # Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:  
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def mostrar_menu(titulo: str, opciones: list[str], tiene_salir: bool = False) -> int:
    
    ejecutado = False
    seleccion = 0
    
    print(f"=== {titulo} ===\n")
    print(f"{colorama.Fore.YELLOW}Use las flechas ↑↓ y ENTER para seleccionar opción\n{colorama.Style.RESET_ALL}")
        
    while True:
        if ejecutado:
            limpiar_lineas_terminal(len(opciones))
            
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(f"➤ {opcion}◄")
            else:
                print(f"  {opcion}")
        
        # Esperar por input
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            if event.scan_code == 72 and seleccion > 0:
                seleccion -= 1
            elif event.scan_code == 80 and seleccion < len(opciones) - 1:
                seleccion += 1
            elif event.scan_code == 28:  # ENTER presionado
                keyboard.clear_all_hotkeys()
                keyboard.remove_all_hotkeys()
                
                # Limpiar el buffer de entrada completamente
                limpiar_buffer_entrada()
                
                # Esperar un momento para que se procese completamente
                time.sleep(0.1)
                
                # Limpiar una vez más por seguridad
                limpiar_buffer_entrada()
                
                if tiene_salir and seleccion == len(opciones) - 1:
                    return None
                else:
                    return seleccion
        ejecutado = True
        
        