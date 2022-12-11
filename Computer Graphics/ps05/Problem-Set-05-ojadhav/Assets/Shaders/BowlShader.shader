Shader "BowlShader"
{
    Properties
    {
    }
    SubShader
    {
        Tags { "RenderType"="Opaque" }
        LOD 100

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
                float4 normal : NORMAL;
            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
                half4 color: COLOR0;
            };

            uniform float3 lightPos;
            uniform float3 cameraPos;
            float4 worldPos;

            float4 color;

            uniform float isOn;


            uniform float3 ambientColor, diffuseColor, specularColor;


            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);

                worldPos = mul(unity_ObjectToWorld, v.vertex);

                if(isOn == 1){
                    float3 L = normalize(lightPos - worldPos);
                    float diffuseComponent = max(dot(v.normal, L),0.0); //Gouraud Smooth Shading
                    float3 C = normalize(cameraPos - worldPos);
                    float3 R = reflect(-L, v.normal); // https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-reflect
                    float specularComponent = pow(max(dot(C, R), 0.0), 8) * 2; //Gouraud Smooth Shading
                    color = float4((ambientColor + diffuseColor*diffuseComponent + specularColor*specularComponent), 1.0);

                    o.color = color;
                }
                else{
                    o.color = half4(diffuseColor, 1.0);
                }

                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                return i.color;
            }
            ENDCG
        }
    }
}
