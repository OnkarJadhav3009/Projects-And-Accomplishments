Shader "MountainTerrainShader"
{
    Properties
    {}
    SubShader
    {
        Tags { "Queue"="Transparent" "RenderType"="Opaque" }
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

            float4 worldPos, worldNormal;


            struct appdata
            {
                float4 vertex : POSITION;
                float4 normal : NORMAL;
            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
                half4 color : COLOR0;
            };

            half4 calculatePhongs(){
                if(isOn == 1){
                    // PHONG ILLUMINATION
                    float3 L = normalize(lightPos - worldPos);
                    float diffuseComponent = max(dot(worldNormal, L),0.0); 
                    float3 C = normalize(cameraPos - worldPos);
                    float3 R = reflect(-L, worldNormal);
                    float specularComponent = pow(max(dot(C, R), 0.0), 8) * 0.2;
                    color = float4((ambientColor + diffuseColor*diffuseComponent
                     + specularColor*specularComponent), 1.0);
                    return color;
                }
                else{
                    return half4(diffuseColor + ambientColor, 1);
                }
            }


            v2f vert (appdata v)
            {
                v2f o;

                v.vertex.y = sin(_Time.y * 0.5 + v.vertex.y) * 10;

                o.vertex = UnityObjectToClipPos(v.vertex);

                worldPos = mul(unity_ObjectToWorld, v.vertex);
                worldNormal = normalize(v.normal);
                
                o.color = calculatePhongs();
                return o;

            }

            fixed4 frag (v2f i) : SV_Target
            {   
                return i.color;
            }
            ENDCG
        }

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

            float4 worldPos, worldNormal;


            struct appdata
            {
                float4 vertex : POSITION;
                float4 normal : NORMAL;
            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
                half4 color : COLOR0;
            };

            half4 calculatePhongs(){
                if(isOn == 1){
                    // PHONG ILLUMINATION
                    float3 L = normalize(lightPos - worldPos);
                    float diffuseComponent = max(dot(worldNormal, L),0.0); 
                    float3 C = normalize(cameraPos - worldPos);
                    float3 R = reflect(-L, worldNormal);
                    float specularComponent = pow(max(dot(C, R), 0.0), 8) * 0.2;
                    color = float4((ambientColor + diffuseColor*diffuseComponent
                     + specularColor*specularComponent), 1.0);
                    return color;
                }
                else{
                    return half4(diffuseColor + ambientColor, 1);
                }
            }


            v2f vert (appdata v)
            {
                v2f o;

                v.vertex.y = cos(_Time.y * 0.5 + v.vertex.y) * 10;

                o.vertex = UnityObjectToClipPos(v.vertex);

                worldPos = mul(unity_ObjectToWorld, v.vertex);
                worldNormal = normalize(v.normal);
                
                o.color = calculatePhongs();
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
