# Results for GITS
 
## Data collection method

* As the project setup is complex for Windows, the testers are required to reserve an Ubuntu instance to ensure an easier setup
* They need to install pip3 on the instance using apt
* After cloning the GITS repository, they install the essential packages using requirements.txt and run the bash script project_init.sh. To ensure gits is successfully installed on the system, the testers can execute the command 'gits hello_world'
* The testers are provided with a pretest, the results of which are used to assess their pre-existing knowledge on Git
* The testers go through the instructions provided and perform the given tasks using Traditional Git, followed by GITS
* The procedure for each tool requires the testers to create a new branch, create a new file, add content to the file and commit to a branch. Meanwhile, the proctor makes a change to the main branch and tester is required to rebase and finally merge the two branches.
* For each of the source control tools, the proctors collect the information regarding the number of commands used to complete the task, the time taken to complete the task and the number of times the tester referred to the source control documentation. 
 
## Challenges Addressed
* To make the implementation process uniform and to avoid any technical difficulty, we made the testers reserve a VCL instance to test the repository.
* We also made sure that each of the testers ran both the commands from traditional git and our gits so that the analysis metrics would be standard
* We also decided to stay on call to assist them with eny technical difficulties even though the documentation was comprehensive.
* There was a small test before the beginning of the debugging session to help us give an idea of the users familiarity with the git syntaxes. 
* To help with the  debug task, we have created a follow me file that answers all the questions: http://tiny.cc/gits
 
## Analysis
The data collected from the lab sessions are tabulated in the this sheet: http://tiny.cc/pznqsz

# ![Data](./etc/data.PNG)
 
The key metrics for comparing the three languages that are implemented are:

1. Number of attempts taken to debug the errors: Considering the average of the total number of attempts for each language, we get the following results:

    * Ruby = 6 (10 people)
    * Rust = 3 (8 people)
    * Go = 4 (9 people)

    It is seen that not everyone was able to debug all the three languages in the time given. According to the data collected, the distribution of the data has high variance. So we propose that median is a better metric than mean to evaluate the languages.

    Median for the number of attempts for all the languages:

    * Ruby = 4.5 
    * Rust = 3
    * Go = 3
 
2. Total time taken to debug: Considering mean of the total time taken is shown below:
    * Ruby = 11.3 mins
    * Rust = 6.12 mins
    * Go = 6 mins

    The corresponding median scores are as follows:
    * Ruby = 13 mins
    * Rust = 6 mins
    * Go = 6 mins

Considering both the metrics (1 and 2), it can be concluded that candidates found Ruby more difficult than the other two. They found Rust and Go equally difficult (but less than Ruby).

# ![Data](./etc/metric.PNG)

 
3. Based on the pretest results and candidates’ feedback: The pretest tested the candidates knowledge of the three languages with 3 simple questions each. The results showed that most people were aware of Ruby. But the results above and the candidates feedback at the end of the session show that most people found Ruby difficult to debug. Hence, the pretest should have been more related to the bugs planted rather than simple questions.
 
4. Based on proctor’s feedback: Based on what we observed on the call, some of the candidates found Ruby difficult (around 4 people), some of them found Go difficult (around 3) and one person found Rust difficult. Two of them went systematically and debugged the codes. For a few candidates, the proctors had to give hints for them to trace the bug.

## Conclusion
Based on all the metrics shown above, we conclude that Rust is the best language among the three chosen for this task. The final order of best to least suitable language for this purpose is Rust, Go and Ruby.
 
## Threats to validity
* Testers have access to the working version of the code in github, which they can use to debug the code.
* The pre test given does not contain equally challenging questions in all languages, which creates a bias.
* The bug introduced in go was easier compared to Rust and Ruby.
* The anomaly with the pre-test score and longer debug time may be because testers guessed the answers for the test

## Materials 
1. The log files for Ruby and Go from the lab sessions can be found in the [LabSessions](./LabSessionData/Attempts) folder
2. The survey sheet used to collect tester's feedback can be found this sheet: http://tiny.cc/xkuosz
3. The data from the attempts file is tabulated for further analysis in this sheet: http://tiny.cc/pznqsz
4. The instructions used to guide the lab activity can be found here: http://tiny.cc/i3oqsz
 
