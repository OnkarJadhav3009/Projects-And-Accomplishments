B581 / Fall 2022, Problem Set 03, Onkar Jadhav, ojadhav

Assets:

    1. Unity version: 
        2020.3.16f
    2. Scripts (C#, .shader): 
        DragObjects.cs - to drag the 2D sprites
        SplineSegmentGPUCompute.cs - to calculate the points to form the spline.
        SplineParameters.cs : contains the information of the spline type and the matrices associated with the respective types.
        SplineShader.shader : contains the vertex shader and the fragment shader. 
    3. Scenes:
        SingleSegmentGPUSpline
        MultipleSegmentGPUSpline_TaskC
    4. GameObjects:
        Line renderer for the control points
        Sprites as control points.

What did I do?:
    
    TASK A:
        1. Duplicated PS02.
        2. Removed the spline line renderer.
        3. Added the c# gpucompute and shader file.
        4. Completed the code using the same logic as ps02.

    TASK B:
        1. Referred Prof. Hanson's lecture notes to obtain the equations for the first and second derivatives of the Bezier, Catmull Rom and B-Spline curves.
        2. Used the equations to draw the respective curves.

    TASK C:
        1. Created multiple spline Segments so that we can manipulate the points as we like.
        2. Added a new C# script which is used to control the Active States of the provided game objects, i.e the control points and the SplineSegment object. 
        3. Also added a function which checks whether the spawn point is valid or not.