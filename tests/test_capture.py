from app.capture_engine.monitor import MonitorManager


def main():

    manager = MonitorManager()

    print("=" * 50)
    print("PKCARDVISION")
    print("=" * 50)

    print(f"\nMonitores: {manager.monitor_count()}\n")

    for index, monitor in enumerate(manager.get_monitors()):
        print(f"Monitor {index}")
        print(monitor)
        print()

    print("Monitor principal:")
    print(manager.get_primary_monitor())


if __name__ == "__main__":
    main()