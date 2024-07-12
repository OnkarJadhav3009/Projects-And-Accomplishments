using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ApplicationManager : MonoBehaviour
{
    public GameObject HUD;
    public GameObject StartScreen, PauseScreen, ThankyouScreen;
    public GameObject MainCam, theBoss, StartCam, DisplayBoss;
    bool GameIsPaused;


    void Start()
    {
        GameIsPaused = false;
        PlayerPrefs.SetFloat("Death", 0);
    }

    public void Quit()
    {
        Application.Quit();
    }

    public void ApplicationStart()
    {
        StartScreen.SetActive(false);
        MainCam.SetActive(true);
        HUD.SetActive(true);
        theBoss.SetActive(true);
        DisplayBoss.SetActive(false);
        StartCam.SetActive(false);
    }

    void Pause()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            GameIsPaused = !GameIsPaused;
        }
        Time.timeScale = GameIsPaused ? 0f : 1f;
        PauseScreen.SetActive(GameIsPaused);
    }

    public void ReloadScene()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    void Update()
    {
        Pause();

        if (PlayerPrefs.GetFloat("Death") == 1)
        {
            HUD.SetActive(false);
            ThankyouScreen.SetActive(true);
        }
    }
}
