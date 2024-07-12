B581 / Fall 2022, Problem-Set 02, Onkar Jadhav, ojadhav


Assets I used for this project:

    1. Unity version: 
        2020.3.16f
    2. Scripts (C#): 
        DragObjects.cs - to drag the 2D sprites
        SplineSegmentCPUCompute.cs - to calculate the points to form the spline.
        SplineParameters.cs : contains the information of the spline type and the matrices associated with the respective types. 
    3. Scenes:
        SingleSegmentCPUSpline
    4. GameObjects:
        Line renderers for the control points and the spline, Sprites as control points.

What did I do?:

    1. In the provided SplineSegmentCPUCompute script, I created a Vector4 uRow which is the matrix of the u parameter. The matrix 'uRow' contains 4 elements ranging 2.from u^3 to a constant 1, decreasing exponentially.
    2. For the control points matrix 'controlMatrix', I assigned Vector4 with values of pos.x, pos.y, pos.z and a constant 1 for each of the control points.
    3. To get the respective spline matrix, I called the GetMatrix method from SplineParameters script. More in "Things I am proud of"...
    4. To calculate the point on the curve, I multiplied the uRow, spline matrix and the control matrix. 

        P = uRow * SplineMatrix * controlMatrix

Things I am proud of:

    1. The bezier matrix was straight forward to calculate, but to calculate the Catmull-Rom and B-Spline, a scalar value was needed to multiply the matrix.
    Unity's Matrix4x4 was not allowing the scalar (float) value to be multiplied to the Matrix4x4 of the spline type matrix. To solve this problem, I created a function that returns a diagonal matrix with the value of x which is a float. (1/2 and 1/6 for Catmull-Rom and B-Spline respectively). While returning the spline matrix for these two types, I multiplied the diagonal matrix with the spline matrix.

    2. I created a horizontal layout and content size fitter for the buttons so that they don't clip out of the screen if the screen size changes. 
