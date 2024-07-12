Shader "CubeShader"
{
    Properties{}

    SubShader
    {

        Pass{
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"

            struct appdata{
                float4 vertex: POSITION;
            };

            struct v2f{
                float4 vertex: SV_POSITION;
            };


            float3 _newPos;
            fixed4 _CubeColor;
            float _theta;
            float2 _scVector;
            float _sr;

            float4x4 getTranslationMatrix(){
                return float4x4(
                    float4(1,0,0,_newPos.x),
                    float4(0,1,0,_newPos.y),
                    float4(0,0,1,_newPos.z),
                    float4(0,0,0,1)
                );
            }

            float4x4 getRotationMatrix(){
                return float4x4(
                    float4(cos(_theta), -sin(_theta), 0, 0),
                    float4(sin(_theta),  cos(_theta), 0, 0),
                    float4(0,0,1,0),
                    float4(0,0,0,1)
                );
            }


            float4x4 getScalingMatrix(){
                return float4x4(
                    float4(_scVector.x, 0, 0, 0),
                    float4(0, _scVector.y, 0, 0),
                    float4(0,0,1,0),
                    float4(0,0,0,1)
                );
            }


            v2f vert(appdata v)
            {                   

                v2f o;
                if(_sr == 0){
                    o.vertex = UnityObjectToClipPos(mul(getTranslationMatrix(), v.vertex));
                }
                else if(_sr == 1){
                    o.vertex = UnityObjectToClipPos(mul(getRotationMatrix(), v.vertex));
                }
                else if(_sr == 2){
                    o.vertex = UnityObjectToClipPos(mul(getScalingMatrix(), v.vertex));
                }
                return o;
            }

            fixed4 frag (v2f i) : SV_Target {
                return _CubeColor;
            } // end of frag shader
            ENDCG
        }
    }
}
