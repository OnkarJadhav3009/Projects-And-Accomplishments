B581 / Fall 2022, Problem Set 04, Onkar Jadhav, ojadhav

Assets:
    1. Unity version: 
        2020.3.16f
    2. Scripts (C#, .shader): 
        DragObjects.cs - control the transformation of the cube, pass the values to the shader.
        CubeShader.shader - perform the gpu side rendering. Use the obtained values from the DragObjects script to create the matrices.
        DrawAxes.cs - draw the axes using gizmos.
    3. Scenes:
        CubeGPURendering
    4. GameObjects:
        Empty GameObject for cube rendering using meshrenderer.
        Canvas for UI
        AXES for axes.

    I created an empty gameobject. Added meshfilter and meshrenderer to it.
    Created a cube by passing its verices and traingles for the mesh into the meshfilter.

    Created a shader for the cube. Material for the cubes meshrenderer was iobttained from this shader.
    In this shader I created 3 matrices for 3 different transformations.
    In the vertex shader, I passed these matrices to perform the opertations. 
    (Scaling and rotaion not working properly)


    
