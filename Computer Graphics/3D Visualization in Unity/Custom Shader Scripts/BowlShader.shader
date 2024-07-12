Shader "BowlShader"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Tags { "Queue"="Transparent" "RenderType"="Opaque" }
        // ZWrite Off
        // Blend SrcAlpha OneMinusSrcAlpha
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
                float2 uv : TEXCOORD0;

            };

            struct v2f
            {
                float4 vertex : SV_POSITION;
                float2 uv : TEXCOORD0;
                float4 normal : TEXCOORD1;
                float4 worldPos : TEXCOORD2;
            };

            uniform float3 lightPos;
            uniform float3 cameraPos;
            float4 worldPos, worldNormal, bumpMapNormal;
            sampler2D _MainTex;
            uniform float4 _MainTex_ST;

            uniform float isOn;

            float4 c;
            
            uniform float3 ambientColor, diffuseColor, specularColor;

            v2f vert (appdata v)
            {
                v2f o;
                
                v.vertex.z += + sin(_Time.z) * 5;
                o.uv = TRANSFORM_TEX(v.uv, _MainTex);
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.normal = normalize(v.normal);
                o.worldPos = mul(unity_ObjectToWorld, v.vertex);

                return o;
            }

            fixed4 frag (v2f i) : COLOR
            {   
                float4 tex1 = tex2D(_MainTex, i.uv);
                float4 normal_N = normalize(tex2D(_MainTex, i.normal));
                if(isOn == 1){
                    float3 L = normalize(lightPos - i.worldPos);
                    float diffuseComponent = max(dot(normal_N, L),0.0); 
                    float3 C = normalize(cameraPos - i.worldPos);
                    float3 R = reflect(-L, i.normal);
                    float specularComponent = pow(max(dot(C, R), 0.0), 32) * 2;
                    c = float4((ambientColor + diffuseColor*diffuseComponent + specularColor*specularComponent), 1.0);
                    return lerp(c, tex1, 0.1);
                }
                else{
                    c = float4((ambientColor), 1.0);
                    return lerp(c, tex1, 0.1);
                }                
            }
            ENDCG
        }
    }
}
