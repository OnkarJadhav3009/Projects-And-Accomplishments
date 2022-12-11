B581 / Fall 2022, Problem Set 05, Onkar Jadhav, ojadhav

Assets:
    1. Unity version: 
        2020.3.16f
    2. Scripts (C#, .shader): 
        DragObjects.cs - control the position of the bowl and the capsule.
        MountainTerrainShader.shader - perform the gpu side rendering. Used the vertices obtained from the cpu side and performed sin function on it to get the bumps and oscilation on the terrain. Also the phong illumination equation is calculated in this file.
        BowlShader.shader -  Basic shader, Additional phong's illumination code.
        GPUComputeTerrain.cs - To compute the terrain using mesh and anding perlin noise to it to get the uneven bumps.
        CPUComputeBowl - Modelled the bowl manually by passing vertices to a mesh.
        RollingBallAlgorithm - contains the algorithm to perform the rotation using the mouse drag.
        DrawAxes.cs - draw the axes using gizmos.
    3. Scenes:
        3D Visualization
    4. GameObjects:
        Ball as capsule
        MountainTerrain
        Bowl
        Canvas for UI
        AXES for axes.


I created a grid mesh with some perlin noise in the cpu side and passed it to the shader. In the Shader I added the sin function to give the mesh a terrain like look.
Created a bowl object. Modelled in the cpu side.

I added the Phong's illumination equation in the shader files so that the terrain and the bowl gets illuminated.

Added a capsule in the scene which can be interacted using the mouse. Also applied Rolling Ball algorithm to the object.

