from apps.cli.app import TunedApp


def main():
    app = TunedApp()
    app.run()


__all__ = ["TunedApp", "main"]
