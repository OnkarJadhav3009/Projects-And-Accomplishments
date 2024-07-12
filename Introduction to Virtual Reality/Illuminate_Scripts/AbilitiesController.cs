using System;
using System.Collections;
using UnityEngine;

public class AbilitiesController : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject lanturn;
    public Light playerLight, directionalLight;
    public float revolveSpeed;
    public float numberOfPoints, nextlevelPoints;
    private bool collected, levelledUp;
    float newPlayerLightRange, newPlayerLightIntensity, finalDirectionalLightIntensity;
    AudioSource audioSource;
    public AudioClip audioClip;
    GameObject newLevelCube;

    void Start()
    {
        // Initialize variables with default values;
        revolveSpeed = 0.0f;
        collected = false;
        levelledUp = false;
        finalDirectionalLightIntensity = 0.0f;
        // Get the Audio Source component of the player
        audioSource = this.GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        // Control the Direction Light's intensity after collecting the final gem 
        directionalLight.intensity = Mathf.Lerp(directionalLight.intensity, finalDirectionalLightIntensity, Time.deltaTime * 0.1f);

        // Trigger active ability by pressing Spacebar to spin a lanturn around the player to illuminate the area around the player
        if (Input.GetKeyDown(KeyCode.Space))
        {
            // Start a coroutine to change the revolve speed of the Lanturn
            StartCoroutine(LanturnSpin());
        }

        // Rotate the lanturn around the player
        lanturn.transform.RotateAround(this.transform.position, new Vector3(0, 1, 0), revolveSpeed * Time.deltaTime);

        // Check if the player has collected a gem or levelled up
        if (collected || levelledUp)
        {
            // Change the range and intensity of the player's Point Light.
            playerLight.range = Mathf.Lerp(playerLight.range, newPlayerLightRange, Time.deltaTime * 2f);
            playerLight.intensity = Mathf.Lerp(playerLight.intensity, newPlayerLightIntensity, Time.deltaTime * 2f);

            if (playerLight.range == newPlayerLightRange && playerLight.intensity == newPlayerLightIntensity)
            {
                collected = false;
            }
        }

        // Condition to check if player has collected all the points available in the level
        if (numberOfPoints == 0)
        {
            playerLight.intensity = 1f;

            // Find the cube using Tag that is blocking the player and change the isTrigger value to TRUE to pass to the next level
            newLevelCube = GameObject.FindGameObjectWithTag("newlvlcube");
            BoxCollider bc = newLevelCube.GetComponent<BoxCollider>();
            bc.isTrigger = true;
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        // Check if the player collides with a gem
        if (other.gameObject.CompareTag("gem"))
        {
            audioSource.PlayOneShot(audioClip);
            // Set the new values of newPlayerLightRange and newPlayerLightIntensity to change player's light
            newPlayerLightRange = playerLight.range + MathF.Sqrt(playerLight.range);
            if (numberOfPoints != 0)
            {
                // Interpolate the light's intensity with the current value and 1
                newPlayerLightIntensity = playerLight.intensity + (1 - playerLight.intensity) / numberOfPoints;
            }
            numberOfPoints -= 1;
            collected = true;
            other.gameObject.SetActive(false); // REF: https://docs.unity3d.com/ScriptReference/GameObject.SetActive.html
        }

        // Check if the player collides with a special gem
        if (other.gameObject.CompareTag("specialgem"))
        {
            audioSource.PlayOneShot(audioClip);
            other.gameObject.SetActive(false);
            // Start a Coroutine to trigger the special powerup
            StartCoroutine(SpecialPowerUp());
        }

        // Check if the player collides with a final gem
        if (other.gameObject.CompareTag("finalgem"))
        {
            audioSource.PlayOneShot(audioClip);
            other.gameObject.SetActive(false);
            // Set the Directional Light's intensity to 1
            finalDirectionalLightIntensity = 1.0f;
        }

        // Check if the player collides with the cube blocking the path to next level
        if (other.gameObject.CompareTag("newlvlcube"))
        {
            // Reset the intensity and range values of the player's Point Light 
            newPlayerLightRange = 5.0f;
            newPlayerLightIntensity = 0.5f;
            numberOfPoints = nextlevelPoints;
        }
    }

    IEnumerator SpecialPowerUp()
    {
        collected = true;
        float ogPLayerLightRange = playerLight.range;
        float ogPLayerLightIntensity = playerLight.intensity;
        newPlayerLightRange = 30f;
        newPlayerLightIntensity = 1.5f;
        yield return new WaitForSeconds(2);
        newPlayerLightIntensity = ogPLayerLightIntensity;
        newPlayerLightRange = ogPLayerLightRange;
    }
    IEnumerator LanturnSpin()
    {
        lanturn.gameObject.SetActive(true);
        revolveSpeed = 90.0f;
        yield return new WaitForSeconds(5);
        revolveSpeed = 0.0f;
        lanturn.gameObject.SetActive(false);
    }
}

