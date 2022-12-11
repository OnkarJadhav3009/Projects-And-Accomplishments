/*  CSCI-B481/B581 - Fall 2022 - Mitja Hmeljak
    Problem Set 02 starting C# program code
    This script should:
    provide the correct parameters in the spline matrices,
    as from the spline Matrix Form.
    
    (defined as in Lecture 11 notes,
     albeit in Lecture 11 the parameter is named 't',
     and here we're naming the parameter 'u',
     following the nomenclature used in the textbook)
                         
    However, keep in mind that Unity Matrix4x4 are "column major",
    as detailed in assignment instructions.
    Original demo code by CSCI-B481 alumnus Rajin Shankar, IU Computer Science.
 */

using UnityEngine;


namespace PS02 {

    public static class SplineParameters    {
    
        public enum SplineType { Bezier, CatmullRom, Bspline }

        public static Matrix4x4 getIDMatrix(float x){
            return new Matrix4x4(
                new Vector4(x, 0f, 0f, 0f),
                new Vector4(0f, x, 0f, 0f),
                new Vector4(0f, 0f, x, 0f),
                new Vector4(0f, 0f, 0f, x)
            );
        }

        public static Matrix4x4 GetMatrix(SplineType type) {
        
            switch (type) {
                
                // TODO: generate Bezier spline matrix,
                //   with constants as per Lecture 11 notes:
                case SplineType.Bezier:
                    return new Matrix4x4( // COLUMN MAJOR!
                        new Vector4(-1f,  3f, -3f, 1f), // TODO
                        new Vector4( 3f, -6f,  3f, 0f), // TODO
                        new Vector4(-3f,  3f,  0f, 0f), // TODO
                        new Vector4( 1f,  0f,  0f, 0f) // TODO
                    );

                // TODO: generate Catmull-Rom spline matrix,
                //   with constants as per Lecture 11 notes:
                case SplineType.CatmullRom:
                    Matrix4x4 cr = new Matrix4x4(
                        new Vector4(-1f,  3f, -3f,  1f),
                        new Vector4( 2f, -5f,  4f, -1f),
                        new Vector4(-1f,  0f,  1f,  0f),
                        new Vector4( 0f,  2f,  0f,  0f)
                    );

                    Matrix4x4 cr_ = getIDMatrix(0.5f);
                    return cr_ * cr;

                // TODO: generate B-spline matrix,
                // with constants as per Lecture 11 notes:
                case SplineType.Bspline:
                    Matrix4x4 bspline = new Matrix4x4(
                        new Vector4(-1f,  3f, -3f,  1f),
                        new Vector4( 3f, -6f,  3f,  0f),
                        new Vector4(-3f,  0f,  3f,  0f),
                        new Vector4( 1f,  4f,  1f,  0f)
                    );

                    Matrix4x4 bspline_ = getIDMatrix((float)1/6);
                    return bspline_ * bspline;

                default:
                    return Matrix4x4.identity;
            }
        } // end of GetMatrix()

        // this could be useful for multi-segment spline curves:
        public static bool UsesConnectedEndpoints(SplineType type) {
            switch (type) {
                case SplineType.Bezier: return true;
                case SplineType.CatmullRom: return false;
                case SplineType.Bspline: return false;
                default: return false;
            }
        } // end of UsesConnectedEndpoints()
        
    } // end of class SplineParameters
    
} // end of namespace PS02