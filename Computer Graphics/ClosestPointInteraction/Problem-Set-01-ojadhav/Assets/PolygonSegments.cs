/*  CSCI-B481/B581 - Fall 2022 - Mitja Hmeljak
    This script will position the start and end points for two line renderers.
    Positioning is done by using GameObject Transforms.
    Used to show closest point on line segment.
    Original demo code by CSCI-B481 alumnus Rajin Shankar, IU Computer Science.
 */

using UnityEngine;

namespace PS01 {

    public class PolygonSegments : MonoBehaviour {

        // fields to connect to Unity objects:
        [SerializeField] private Transform subjectPointTransform;
        [SerializeField] private Transform[] PolygonPoints;
        [SerializeField] private LineRenderer[] subjectLineRenderers;
        [SerializeField] private LineRenderer connectingLineRenderer;

        // Update() is called once per frame:
        private void Update() {
            for (int i = 0; i < PolygonPoints.Length; i++) {
                int j = (i + 1) % PolygonPoints.Length;
                subjectLineRenderers[i].SetPosition(0, PolygonPoints[i].position);
                subjectLineRenderers[i].SetPosition(1, PolygonPoints[j].position);
            }

            Vector2 lClosestPoint = LineUtility.ClosestPointOnPolygon(PolygonPoints, subjectPointTransform.position);

            connectingLineRenderer.SetPosition(0, subjectPointTransform.position);
            connectingLineRenderer.SetPosition(1, lClosestPoint);
        } // end of Update()

    } // end of class SingleSegmentPositionLines

} // end of namespace PS01