using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using TMPro;
using UnityEngine.UI;


public class Simulator : MonoBehaviour
{
    public GameObject SimulationScreen;
    public List<Contestant> contestants;
    public List<Tribe> tribes;
    public GameObject EventPrefab;
    public GameObject EventScreen;
    // Start is called before the first frame update
    private Button button;
    
    public void StartSimulation(){
        Debug.Log("Simulation Started");

        foreach (var contestant in contestants)
        {
            foreach (var contestant2 in contestants)
            {
                if (contestant != contestant2)
                {
                    contestant.AddRelationship(new Relationship(contestant2));
                }
            }
        }
        Simulate();
    }
    // Update is called once per frame
    void Update()
    {
        
    }
    public void Simulate()
    {
        Destroy(GameObject.Find("Event(Clone)"));

        GameObject.Find("StartScreen").SetActive(false);
        SimulationScreen.SetActive(true);
        foreach (var Tribe in tribes)
        {
            foreach (var contestant in Tribe.TribeSelector.GetComponent<TribeSelector>().TribeSlots)
            {
                Tribe.tribeMembers.Add(contestants.Find(c => c.name == contestant.name));
            }
        }
        AllyEvent AllyEvent = PickEvent(tribes[0].tribeMembers[new System.Random().Next(0,8)], tribes[0].tribeMembers[new System.Random().Next(0,8)]);
        Debug.Log("Ally Event: " + AllyEvent);
        CreateEventVisual(AllyEvent);
       // EventScreen.SetActive(false);

        
    }
    public string[] posAllies = { "Find Something in Common","Bond Strongly","Bond Slightly"};
    public string[] negAllies = { "Have a Minor Disagreement","Has a Major Meltdown","Have a Small Fight","Have a Major Disagreement","Have a Major Fight"};
    AllyEvent PickEvent (Contestant C1 , Contestant C2)
    {
        float mod = UnityEngine.Random.Range (-1.0f, 1.0f);
        string desc;
        if (mod > 0) 
        { 
            desc = posAllies[new System.Random().Next(0, posAllies.Length)];
        } 
        else { desc = negAllies[new System.Random().Next(0, negAllies.Length)]; } 
        Debug.Log(desc);
        AllyEvent AllyEvent = new AllyEvent(mod,desc,C1,C2);
        Debug.Log(C1.name+" and " +C2.name+" "+AllyEvent.ToString());
        return AllyEvent;
    }
    void CreateEventVisual(AllyEvent AllyEvent)
    {
        GameObject event1 = Instantiate(EventPrefab);
        event1.GetComponent<RectTransform>().SetParent(SimulationScreen.GetComponent<RectTransform>());
        event1.transform.localScale = Vector3.one;
        event1.transform.GetChild(0).GetComponent<TMP_Text>().text = AllyEvent.contestant1.name + " and " + AllyEvent.contestant2.name + " " + AllyEvent.ToString();
        event1.transform.GetChild(1).GetComponent<Image>().sprite = AllyEvent.contestant1.Image.GetComponent<Image>().sprite;
        event1.transform.GetChild(2).GetComponent<Image>().sprite = AllyEvent.contestant2.Image.GetComponent<Image>().sprite;
    }
}
