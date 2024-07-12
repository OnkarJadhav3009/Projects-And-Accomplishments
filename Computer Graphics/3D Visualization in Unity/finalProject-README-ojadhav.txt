B581 / Fall 2022, Final Project, Onkar Jadhav, ojadhav

Assets:
    1. Unity version: 
        2020.3.16f
    2. Scripts (C#, .shader): 
        DragObjects.cs - control the position of the capsule.
        MountainTerrainShader.shader - perform the gpu side rendering, Additional the phong's illumination code is written in this.
        BowlShader.shader -  Basic shader, Additionally, the phong's illumination code is written this.
        Capsule.shader - To render the texture on the capsule.
        GPUComputeTerrain.cs - To compute the terrain using mesh and passing it to gpu.
        CPUComputeBowl - Modelled the bowl manually by passing vertices to a mesh.
        RollingBallAlgorithm - contains the algorithm to perform the rotation using the mouse drag.
        DragObjects.cs - contains the algorithm to perform click and drag operations on the object attached.
        DrawAxes.cs - draw the axes using gizmos.
    3. Scenes:
        3D Visualization
    4. GameObjects:
        Capsule
        MountainTerrain
        Bowl
        Canvas for UI
        AXES for axes.

TITLE : INFINITE MOUNTAINS

A] 3D Modelling and Rendering:

    1. Created a flat mesh algorithmically, using for loops. Did not manipulate the y coordinate of the mesh, as it was to be done in the shader. Therefore, In the GPU side code, I set the y coordinate of the vertex to the tan of the multiplication of its x and z coordinates. 

        v.vertex.y = tan(v.vertex.x * v.vertex.z)
    
    By doing this mathematics, "INFINITE MOUNTAINS" can be simulated.

    2. For the CPU side object, I created a bowl shape. I animated the z coordinate of the vertex in the shader file.

B] Interaction:

    1. The Capsule in the scene has a DragObjects script attached. It is used to drag the object anywhere in the scene. To add fun, added a capsule collider so that, we can try to put the capsule in the bowl.

    2. The Bowl in the scene has a RollingBallAlgorithm script attached. It is used to rotate the object. It also has a mesh collider.

C] Camera:

    1. After pressing the play button, the main camera is moved around on a spline path. Using 4 control points I calculated the positions of the spline and instead of rendering the spline, I passed these points as moves for the camera. 

    2. After reaching the final control point the camera becomes stationery and then you can move around the camera yourselves using mouse and keys.

D] Illumination:

    Implemented the Phong's illumination for the terrain and the bowl objects.

    DiffuseComponent = SurfaceNormal . LightDirection
    SpecularComponent = CameraDirection . ReflectionDirection

    final color = ambientColor + DiffuseColor * DiffuseComponent + SpecularColor * SpecularComponent

E] Mapping:

    Texture mapped two objects in the scene using unlit shaders. Capsule and the Bowl.