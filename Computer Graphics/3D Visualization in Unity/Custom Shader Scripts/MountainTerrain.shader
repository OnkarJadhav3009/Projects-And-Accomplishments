Shader "MountainTerrainShader"
{
    Properties
    {
    }
    SubShader
    {
        Tags { "Queue"="Transparent" "RenderType"="Transparent" }
        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"


            float4 color;

            uniform float3 lightPos;
            uniform float3 cameraPos;

            uniform float isOn;

            uniform float3 ambientColor, diffuseColor, specularColor;

            uniform float _Intensity;


            struct appdata
            {
                float4 vertex : POSITION;
                float4 normal : NORMAL;
            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
                float4 normal : TEXCOORD0;
                float4 worldPos : TEXCOORD1;
            };

            v2f vert (appdata v)
            {
                v2f o;

                v.vertex.y = tan(v.vertex.x * v.vertex.z * 2) * 0.5;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.normal = v.normal;
                o.worldPos = mul(unity_ObjectToWorld, v.vertex);

                return o;

            }

            fixed4 frag (v2f i) : SV_Target
            {   
                if(isOn == 1){
                    // PHONG ILLUMINATION
                    float3 L = normalize(lightPos - i.worldPos);
                    float diffuseComponent = max(dot(i.normal, L),0.0); 
                    float3 C = normalize(cameraPos - i.worldPos);
                    float3 R = reflect(-L, i.normal);
                    float specularComponent = pow(max(dot(C, R), 0.0), 32) * _Intensity;
                    color = float4((ambientColor + diffuseColor*diffuseComponent
                     + specularColor*specularComponent), 1.0);
                    return color;
                }
                else{
                    return half4(ambientColor, 1);
                }
            }
            ENDCG
        }
    }
}
