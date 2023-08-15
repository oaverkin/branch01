import omni.ext
import omni.ui as ui


class KitExtTestExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[omni.example.spawn_prims] MyExtension startup")
        with ui.ScrollingFrame():
            self.mesh_window()
            self.shape_window()

    def mesh_window(self):
        self._mesh_window = ui.Window("Create Mesh", width=200, height=300)
        with self._mesh_window.frame:
            with ui.VStack():
                def add_mesh(prim_type):
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                                              prim_type=prim_type)

                ui.Button("Spawn Cube", clicked_fn=lambda: add_mesh("Cube"))
                ui.Button("Spawn Cone", clicked_fn=lambda: add_mesh("Cone"))
                ui.Button("Spawn Cylinder", clicked_fn=lambda: add_mesh("Cylinder"))
                ui.Button("Spawn Disk", clicked_fn=lambda: add_mesh("Disk"))
                ui.Button("Spawn Plane", clicked_fn=lambda: add_mesh("Plane"))
                ui.Button("Spawn Sphere", clicked_fn=lambda: add_mesh("Sphere"))
                ui.Button("Spawn Torus", clicked_fn=lambda: add_mesh("Torus"))
    
    def shape_window(self):
        self._shape_window = ui.Window("Create Shape", width=200, height=300)
        with self._shape_window.frame:
            with ui.VStack():
                def on_click(prim_type):
                    omni.kit.commands.execute('CreatePrimWithDefaultXform',
                                              prim_type=prim_type)

                ui.Button("Spawn Capsule", clicked_fn=lambda: on_click("Capsule"))

    def on_shutdown(self):
        print("[omni.example.spawn_prims] MyExtension shutdown")
