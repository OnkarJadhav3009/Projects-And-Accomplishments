/*  CSCI-B481/B581 - Fall 2022 - Mitja Hmeljak

    The Vertex Shader component in this Unity Shader should:

    use t1, t2 values to compute the position of each 
       vertex on the Spline Curve:
    t1 is for the "base curve",
    t2 is for the "offset curve".

    to calculate (on the GPU) the vertices on a single Spline Curve segment,
    to be displayed as a Mesh, using a Mesh Renderer.

    Original demo code by CSCI-B481 alumnus Rajin Shankar, IU Computer Science.
 */




Shader "SplineVertexShader" {

    Properties { }
    
    SubShader {
    
        cull off
        
        Tags { "RenderType"="Opaque" "Queue"="Transparent" }
        
        Pass  {
        
            CGPROGRAM
            
            // we'll provide both Vertex and Fragment shaders:
            #pragma vertex vert
            #pragma fragment frag
            
            #include "UnityCG.cginc"

            // note: in GLSL the following struct of variables
            //     would have the "attribute" qualifier,
            //     as received by the vertex shader
            //     and unique for each vertex shader instance:
            struct appdata {
                float4 vertex : POSITION;
            };

            // note: in GLSL the following struct of variables
            //     would have the "varying" qualifier,
            //     as passed from the vertex shader
            //     to the fragment shader:
            struct v2f {
                float4 vertex : SV_POSITION;
            };
            
            // note: in GLSL the following parameters
            //     would have the "uniform" qualifier:
            
            // here we receive (from application, CPU side) the spline Hermite form matrix:
            float4x4 _SplineMatrix;
            
            // here we receive (from application, CPU side) the four control points:
            float2 _Control0, _Control1, _Control2, _Control3;
            
            // here we receive (from application, CPU side) how many steps there should be on curve:
            float _Step;
            
            

            // ---------------------------------------------------------
            // the spline equation calculation happens here, i.e.:
            // you need to compute the spline multiplication as from the matrix form
            // as per Problem Set 03 instructions,
            // in the form p(u) = uT * M * p
            //   
            //   Note: matrices are defined in "column major" !
            //
            //   Note2: here we name the parameter t instead of u
            //
            float4 HermiteMult(float4x4 controlP, float4x4 splineM, float4 tParamsVector) {
                //
                // TODO - compute vertex on curve:
                //
                // float4x4 res = mul(splineM, controlP);
                // float4 vertexOnCurve = mul(tParamsVector, res);
                float4 vertexOnCurve = mul(tParamsVector, mul(transpose(splineM), controlP));
                return vertexOnCurve;
            } // end of HermiteMult()



            // ---------------------------------------------------------
            // compute the Normal to the curve, at vertex provided by parameter t:
            // 
            float2 GetNormalToCurve(float t, float dt, float4x4 controlMatrix, float4x4 splineMatrix) {
                //
                // TODO - compute normal to segment (p1, p2) on curve
                //        where p1 is the vertex on curve at parameter t
                //        where p2 is the vertex on curve at parameter t2 = t + dt
                //
                // ADDITIONAL NOTE:
                //      The resulting normal should be normalized before returning it!
                //      And the returned value should be a float2 (not a float4!)
                //
                float4 t_mat = float4(t*t*t, t*t, t, 1);

                float x = t+dt;
                float4 dt_mat = float4(x*x*x, x*x, x, 1);

                float4 start = mul(t_mat, mul(splineMatrix, controlMatrix));
                float4 end = mul(dt_mat, mul(splineMatrix, controlMatrix));

                float2 P = (end - start).xy; 

                float2 normal = float2(-P.y, P.x);
                
                return normalize(normal);
            }  // end of GetNormalToCurve()
            


            // ---------------------------------------------------------
            // the Vertex Shader outputs one vertex position on the Spline Curve:
            v2f vert (appdata v) {
            
                // the output to this shader is:
                v2f o;
                
                // in the vertex shader,
                //  we receive t in the x parameter,
                //  and the offset in the y parameter:
                float t = v.vertex.x;
                float offset = v.vertex.y;
                float4 tRow = float4(t*t*t, t*t, t, 1);
                

                //
                // TODO - compute matrix of four Control Points for spline:
                //
                float4 p0 = float4(_Control0.x, _Control0.y, 0, 1);
                float4 p1 = float4(_Control1.x, _Control1.y, 0, 1);
                float4 p2 = float4(_Control2.x, _Control2.y, 0, 1);
                float4 p3 = float4(_Control3.x, _Control3.y, 0, 1);

                float4x4 controlMatrix = float4x4(p0, p1, p2, p3);

                // call HermiteMult to perform the spline equation calculation,
                // to obtain the position of the point on the spline "base" curve:
                float4 worldPosition = HermiteMult(controlMatrix, _SplineMatrix, tRow);

                // calculate the normal, used for the equivalent point on offset curve:
                float2 normal = GetNormalToCurve(t, _Step, controlMatrix, _SplineMatrix);

                // the following will do nothing when offset is 0,
                //         i.e. vertex on "base curve",
                // but it will move the vertex in the direction of the normal
                //         for the vertex on "offset curve":
                worldPosition.xy += normal * offset;

                worldPosition.z = 0;
                worldPosition.w = 1;

                o.vertex = mul(UNITY_MATRIX_VP, worldPosition);

                return o;
            } // end of vert shader


            // -------------------------------------------------
            // the Fragment Shader simply outputs a fixed color:

            fixed4 _Color;

            fixed4 frag (v2f i) : SV_Target {
                return _Color;
            } // end of frag shader

            ENDCG
        }
    }
}