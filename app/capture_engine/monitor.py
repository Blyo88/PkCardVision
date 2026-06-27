from typing import Dict, List

from mss import mss


class MonitorManager:

    def __init__(self) -> None:
        self._mss = mss()

    def get_monitors(self) -> List[Dict]:
        return self._mss.monitors

    def get_primary_monitor(self) -> Dict:
        return self._mss.monitors[1]

    def get_monitor(self, index: int) -> Dict:
        monitors = self._mss.monitors

        if index < 1 or index >= len(monitors):
            raise IndexError(
                f"Monitor {index} no encontrado. "
                f"Hay {len(monitors) - 1} monitor(es) disponibles."
            )

        return monitors[index]

    def monitor_count(self) -> int:
        return len(self._mss.monitors) - 1