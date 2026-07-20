"""
Menú Principal de la Aplicación
Interfaz de usuario en terminal
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from config.settings import Settings
from config.logger_config import logger
from config.constants import MENSAJES
from data.binance_connector import obtener_connector
from core.indicators import IndicadoresTecnicos
from core.signals import GeneradorSeñales
from devops.monitoring import system_monitor
import sys

class MenuPrincipal:
    """Menú principal de la aplicación"""
    
    def __init__(self, settings: Settings, monitor):
        """Inicializa el menú"""
        self.settings = settings
        self.monitor = monitor
        self.console = Console()
        self.binance = obtener_connector()
        self.ejecutando = True
    
    def ejecutar(self):
        """Ejecuta el loop principal del menú"""
        while self.ejecutando:
            try:
                self._mostrar_menu_principal()
                opcion = input("\n➜ Ingresa opción (0-9): ").strip()
                self._procesar_opcion(opcion)
            except KeyboardInterrupt:
                self.console.print("\n\n🛑 Aplicación interrumpida por el usuario")
                break
            except Exception as e:
                logger.error(f"❌ Error en menú: {str(e)}")
                self.console.print(f"\n❌ Error: {str(e)}")
    
    def _mostrar_menu_principal(self):
        """Muestra el menú principal"""
        self.console.clear()
        
        # Banner
        banner = Panel(
            "[bold cyan]🚀 SISTEMA INTELIGENTE DE TRADING XRP/USDT[/bold cyan]\n"
            "[cyan]Versión 2.0 | Análisis Técnico + IA[/cyan]",
            style="bold blue"
        )
        self.console.print(banner)
        
        # Estado
        estado = Panel(
            f"[green]✓ Sistema Operativo[/green]\n"
            f"[cyan]Símbolo: {self.settings.TRADING_SYMBOL}[/cyan]\n"
            f"[cyan]Intervalo: {self.settings.TRADING_INTERVAL}[/cyan]",
            style="green"
        )
        self.console.print(estado)
        
        # Menú opciones
        self.console.print("\n[bold]📋 OPCIONES:[/bold]\n")
        self.console.print("  [1] 📊 Análisis Técnico Detallado")
        self.console.print("  [2] ⏱️  Monitoreo Continuo (5 min)")
        self.console.print("  [3] ⚡ Modo Agresivo (1 min)")
        self.console.print("  [4] ⚙️  Configuración Avanzada")
        self.console.print("  [5] 📈 Histórico & Estadísticas")
        self.console.print("  [6] 💾 Gestionar Alertas")
        self.console.print("  [7] 🛡️  Seguridad & API")
        self.console.print("  [8] 🔌 Estado del Sistema")
        self.console.print("  [0] ❌ Salir\n")
    
    def _procesar_opcion(self, opcion: str):
        """Procesa la opción seleccionada"""
        opciones = {
            '1': self._analisis_detallado,
            '2': self._monitoreo_continuo,
            '3': self._modo_agresivo,
            '4': self._configuracion,
            '5': self._historico,
            '6': self._alertas,
            '7': self._seguridad,
            '8': self._estado_sistema,
            '0': self._salir
        }
        
        func = opciones.get(opcion)
        if func:
            func()
        else:
            self.console.print("\n[red]❌ Opción no válida[/red]")
            input("\nPresiona ENTER para continuar...")
    
    def _analisis_detallado(self):
        """Muestra análisis detallado"""
        try:
            self.console.print("\n[bold cyan]📊 OBTENIENDO ANÁLISIS...[/bold cyan]")
            
            # Obtener datos
            df = self.binance.obtener_velas(
                self.settings.TRADING_SYMBOL,
                self.settings.TRADING_INTERVAL,
                self.settings.CANDLES_LIMIT
            )
            
            if df is None:
                self.console.print("[red]❌ Error al obtener datos[/red]")
                return
            
            # Calcular indicadores
            df = IndicadoresTecnicos.calcular_todos(df)
            
            # Generar señal
            señal = GeneradorSeñales.generar_señal(df)
            
            if señal:
                self._mostrar_analisis(señal)
            else:
                self.console.print("[red]❌ Error generando análisis[/red]")
        
        except Exception as e:
            logger.error(f"❌ Error en análisis: {str(e)}")
            self.console.print(f"[red]❌ Error: {str(e)}[/red]")
        
        input("\nPresiona ENTER para continuar...")
    
    def _mostrar_analisis(self, señal: dict):
        """Muestra el análisis de forma presentable"""
        # Tabla de indicadores
        tabla = Table(title="📊 INDICADORES TÉCNICOS")
        tabla.add_column("Indicador", style="cyan")
        tabla.add_column("Valor", style="green")
        
        for key, value in señal['indicadores'].items():
            if value is not None:
                tabla.add_row(key.upper(), f"{value:.4f}")
        
        self.console.print(tabla)
        
        # Recomendación
        panel_recom = Panel(
            f"[bold]{señal['emoji']} {señal['recomendacion']}[/bold]\n"
            f"Score: {señal['score']}/100\n"
            f"Precio: ${señal['precio']:.4f}",
            style="bold yellow"
        )
        self.console.print(panel_recom)
        
        # Señales detalladas
        self.console.print("\n[bold]🔍 SEÑALES DETALLADAS:[/bold]")
        for señal_item in señal['señales']:
            self.console.print(f"  {señal_item}")
    
    def _monitoreo_continuo(self):
        """Inicia monitoreo continuo"""
        self.console.print("\n[bold yellow]⏱️  MONITOREO CONTINUO (5 minutos entre chequeos)[/bold yellow]")
        self.console.print("[dim]Presiona CTRL+C para detener...\n[/dim]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _modo_agresivo(self):
        """Modo agresivo (1 minuto)"""
        self.console.print("\n[bold red]⚡ MODO AGRESIVO (1 minuto entre chequeos)[/bold red]")
        self.console.print("[dim]Presiona CTRL+C para detener...\n[/dim]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _configuracion(self):
        """Configuración avanzada"""
        self.console.print("\n[bold]⚙️  CONFIGURACIÓN AVANZADA[/bold]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _historico(self):
        """Histórico y estadísticas"""
        self.console.print("\n[bold]📈 HISTÓRICO & ESTADÍSTICAS[/bold]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _alertas(self):
        """Gestión de alertas"""
        self.console.print("\n[bold]💾 GESTIONAR ALERTAS[/bold]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _seguridad(self):
        """Seguridad y API"""
        self.console.print("\n[bold]🛡️  SEGURIDAD & CREDENCIALES[/bold]")
        # Implementación completa en siguiente paso
        input("Presiona ENTER para continuar...")
    
    def _estado_sistema(self):
        """Estado del sistema"""
        self.console.print("\n[bold]🔌 ESTADO DEL SISTEMA[/bold]")
        estado = system_monitor.obtener_estado()
        if estado:
            tabla = Table(title="MÉTRICAS DEL SISTEMA")
            tabla.add_column("Métrica", style="cyan")
            tabla.add_column("Valor", style="green")
            
            for key, value in estado.items():
                tabla.add_row(key.upper(), str(value))
            
            self.console.print(tabla)
        input("\nPresiona ENTER para continuar...")
    
    def _salir(self):
        """Salir de la aplicación"""
        self.console.print("\n[yellow]👋 Gracias por usar el Sistema de Trading XRP/USDT[/yellow]")
        self.console.print("[dim]Cerrando aplicación...[/dim]\n")
        self.ejecutando = False
        sys.exit(0)
