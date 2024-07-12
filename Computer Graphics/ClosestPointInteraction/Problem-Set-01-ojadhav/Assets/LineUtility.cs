/*  CSCI-B481/B581 - Fall 2022 - Mitja Hmeljak
    This script provides a library of "utility" methods,
    that may be useful to solve Problem Set 01.
    
    However, you may have to complete the parts marked as TODO ...
    Original demo code by CSCI-B481 alumnus Rajin Shankar, IU Computer Science.
 */

using UnityEngine;

namespace PS01 {

    public static class LineUtility {
    
        // DirectionNormal() --- returns the normal to a given direction vector:
        public static Vector2 DirectionNormal(Vector2 direction) {
            // TODO: compute 
            //  Vector2 normal = ...
            //  return normal;
            // normal n = (-(y2-y1), (x2-x1))
            // Debug.Log(direction + "---------------------------DIRECTION");
            Vector2 normal = new Vector2(-direction.y, direction.x);
            // Debug.Log(normal + "---------------------------NORMAL");
            return normal;


        } // end of DirectionNormal() 

        // LineSegmentNormal() --- returns the normal to a line segment:
        public static Vector2 LineSegmentNormal(Vector2 start, Vector2 end) {
            // TODO: compute 
            //  Vector2 direction =  ...
            //  Vector2 normal = ...
            //  return normal;
            Vector2 direction = new Vector2((end.x - start.x), (end.y - start.y));
            Vector2 normal = DirectionNormal(direction);
            return normal;
        } // end of LineSegmentNormal()


        // ClosestPointOnLine() --- returns the closest point on a line to a given query point:
        public static Vector2 ClosestPointOnLine(Vector2 pointOnLine, Vector2 direction, Vector2 point) {
            // TODO: compute 
            //
            // ERRATA CORRIGE:
            //  Vector2 localX = ...  <- incorrect, it should be a float
            //  float localX = ...    <- correct type definition
            // point : x0, y0 ,,,, direction :n ,,,,,,,pointOnLine : x1,y1

            // REAL TODO!
            // 1. Calculate vector AC: pointOnLine - point
            // 2. Get the dot product between direction and ac
            // 3. Get P using : x1 + l x v
            Vector2 ac = new Vector2((point.x - pointOnLine.x), (point.y - pointOnLine.y));
            float l = Vector2.Dot(direction, ac);
            Vector2 P = pointOnLine + (l*direction);
            return P;
            //  return ...
            
            //  you may find useful the 2D Point-Line Geometry expressions shown at lecture time
            //  
        } // end of ClosestPointOnLine()


        // ClosestPointOnSegment() --- returns the closest point (on a line segment)
        //                             to a given subject point:
        public static Vector2 ClosestPointOnSegment(Vector2 start, Vector2 end, Vector2 point) {
            // TODO: 
            //  you may find the above methods useful, once you complete them...
            Vector2 vector_v = end - start;
            Vector2 v = vector_v/vector_v.magnitude;
            Vector2 P = ClosestPointOnLine(start, v, point);
            // Debug.Log((P.x, P.y)+ "--------------------------P");
            // Vector2 AC = new Vector2((point.x - start.x), (point.y));
            Vector2 ac = point - start;

            float l = Vector2.Dot(v, ac);

            if (l < 0) {
                return start;
            }
            else if (l > vector_v.magnitude){
                return end;
            }
            return P;
        } // end of ClosestPointOnSegment()



        // NOTE: look at the two method implementations below, and 
        //       decide whether you prefer to use:
        //       either the ClosestPointOnPolygon() method using Vector2[] polygonPoints
        //       or the ClosestPointOnPolygon() method using Transform[] polygonVertices,
        //       but not both!
        
        
        // ClosestPointOnPolygon() --- returns the closest point (on a polygon)
        //                             to a given query point.
        
        // Note:
        //   Polygon given as array of vertices with vertex[n-1] connecting back to vertex[0]
        // public static Vector2 ClosestPointOnPolygon(Vector2[] polygonPoints, Vector2 point) {
        //     Vector2 result = Vector2.zero;
        //     float minSqrDistance = float.PositiveInfinity;
        //     for (int i = 0; i < polygonPoints.Length; i++) {
        //         int j = (i + 1) % polygonPoints.Length;
        //         Vector2 side = polygonPoints[j] - polygonPoints[i];
        //         float sideLength = side.magnitude;
        //         Vector2 sideDirection = side / sideLength;

        //         Vector2 start = polygonPoints[i];
        //         Vector2 end = polygonPoints[j];
        //         Vector2 ac = new Vector2((point.x - start.x), (point.y - start.y));
        //         float l = Vector2.Dot(sideDirection, ac);
        //         Vector2 P = start + (l*side);

        //     // TODO: 
        //     //  you may find useful the utility methods at the top of this file, once you complete them...

        //         Vector2 pointOnPolygon;
        //         if (l < 0) {
        //             pointOnPolygon = start;
        //         } else if (l > side.x){
        //             pointOnPolygon = end;
        //         } else {
        //             pointOnPolygon =  P;
        //         }

        //     // TODO:
        //     //  the following code works, as long as you computed pointOnPolygon correctly.
        //     //  It will be useful to understand what the following lines do:
        //         Vector2 delta = point - pointOnPolygon;
        //         float sqrDistance = delta.sqrMagnitude;

        //         if (sqrDistance < minSqrDistance) {
        //             result = pointOnPolygon;
        //             minSqrDistance = sqrDistance;
        //         }
        //     }
            // return result;
        // } // end of ClosestPointOnPolygon()


        // // ClosestPointOnPolygon() --- returns the closest point (on a polygon)
        // //                             to a given subject point.
        // //  Note:
        // //      the polygon is given as array of transforms
        // //      with vertex[n-1] connecting back to vertex[0]
        // //
        public static Vector2 ClosestPointOnPolygon(Transform[] polygonVertices, Vector2 point) {
        
            Vector2 result = Vector2.zero;
            float minSqrDistance = float.PositiveInfinity;
            
            for (int i = 0; i < polygonVertices.Length; i++) {
                int j = (i + 1) % polygonVertices.Length;
                Vector2 side = polygonVertices[j].position - polygonVertices[i].position;
                float sideLength = side.magnitude;
                Vector2 sideDirection = side / sideLength;
                
                Vector2 start = polygonVertices[i].position;
                Vector2 end = polygonVertices[j].position;

                Vector2 ac = point - start;
                float l = Vector2.Dot(sideDirection, ac);
                Vector2 P = ClosestPointOnLine(start, sideDirection, point);

            // TODO: 
            //  you may find useful the utility methods at the top of this file, once you complete them...

                Vector2 pointOnPolygon;
                if (l < 0) {
                    pointOnPolygon = start;
                } else if (l > sideLength){
                    pointOnPolygon = end;
                } else {
                    pointOnPolygon = P;
                }
            // TODO:
            //  the following code works, as long as you computed pointOnPolygon correctly.
            //  It will be useful to understand what the following lines do:
                Vector2 delta = point - pointOnPolygon;
                float sqrDistance = delta.sqrMagnitude;

                if (sqrDistance < minSqrDistance) {
                    result = pointOnPolygon;
                    minSqrDistance = sqrDistance;
                }
            }
            return result;
        } // end of ClosestPointOnPolygon()


    } // end of static class LineUtility

} // end of namespace PS01