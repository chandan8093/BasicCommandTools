# Basic Concepts -
```
    .circleci/config.yml
    1.Job 
        - Atomic unit of work
        - Ex : unit test,build/compile,Lint,Deploy etc
    2.Job consists of 
        -  Executer : Execution Environment(container or VM ruunig with specified steps)
        -  steps    : Actions and commands(run commands and scripts)
    3.Workflow
        -  one or more jobs that form a full process
        -  step dependencies b/w jobs 
    4.PipeLine
        -  A trigger/run of workflow
        -  pipelines have multiple workflows        

```


# Official Documentation :
```https://circleci.com/docs/gitlab-integration```