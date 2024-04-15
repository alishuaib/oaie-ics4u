from .demo import show_demo

try:
    import micropip
    async def installation():
        await micropip.install('ipywidgets')
        await micropip.install('pillow')
    installation()
except ImportError:
    print("No micropip (Pyodide env) found, skipping installation of dependencies")