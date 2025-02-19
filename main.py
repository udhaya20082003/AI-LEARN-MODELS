import os
import torch
from dotenv import load_dotenv 
from model_utils import Chatbot , Llm_EndPoint
from document_prompts_utils import embedding_model
from model_utils import get_completion
from question_generation_utils import load_generation_generation_model , question_generation_query
load_dotenv() # Load Secret Keys out side the repo

context = '''  From now onwards we will start with the unit 6 that is conditionals and loops.
 And in this particular lecture we will talk about the if-else construct, nested if construct
 and else if construct.
 We will consider what these constructs are and when to use these constructs.
 So let's get started.
 Let's start with our first construct that is if-else construct.
 In order to understand if-else construct, let me give you one real-world example.
 As you can see this is an interface of an Android operating system.
 Now we already know that if we click on this button then the applications page will get
 opened up.
 Therefore we can say that opening up of this applications page is actually dependent on
 that round button clicking.
 But how can we relate this concept to if-else?
 If this button is clicked then the applications page will get opened up, right?
 Else you will simply stay at home page.
 Isn't that so?
 Because opening up of this applications page is actually dependent on this button clicking,
 therefore we can actually use if-else construct here.
 Whenever something is dependent on something then we can use if-else construct.
 Now let's try to understand what is nested if and when to use nested if.
 Then let's consider our real-world example that is Android operating system interface.
 When you click on this button then the applications page will get opened up.
 And suppose I want to open up an application like suppose Play Store then I need to click
 on this button and the Play Store will get opened up.
 Now you might ask me this question how we can relate this concept to nested if and why
 I am telling all this?
 Simple, if you click on this button that is this round button then the applications page
 will get opened up, right?
 You know that already.
 After that if you click on this Play Store button then the Play Store will get opened
 up.
 That means if you really want to open up the Play Store you first have to click on this
 button then only you would be able to click on this button.
 Isn't that so?
 This whole if construct is dependent on this if construct.
 Therefore it has to be put inside of this if construct.
 Whenever there is an if construct inside another if construct then it is called nested if construct.
 Please remember this point.
 We cannot put this outside of this if construct because the only way you would be able to
 access this Play Store button is by clicking on this button.
 If you won't click on this button you will simply stay at home page, right?
 So we can easily see how this nested if construct is useful in our real world application like
 Android operating system.
 Now let's consider why to use else if and when to use else if.
 Then we will consider real world example that is Android operating system.
 Suppose Android operating system provides you the facility to add shortcuts in your
 home screen itself.
 As you can see here these are the shortcuts, right?
 This is camera application button, this is contacts application button and this is Chrome
 application button.
 Now instead of clicking this button if we simply click on this button then the Chrome
 application will open up, right?
 How I can relate this concept to else if?
 If this round button is clicked then definitely application page will get opened up but if
 we directly click on this button that is Chrome application button then Google Chrome
 will get opened up.
 Therefore whenever we have no dependency we can use else if.
 As this button clicking event is not dependent on this button clicking event so we can use
 else if construct, right?
 Now it's time for most frequently asked questions that is FAQs.
 Is it necessary to put the else part?
 Now somebody asked me this question is it really necessary to put the else part after
 the if part?
 The answer to this question is no and yes both at the same time.
 Let's try to understand this with the help of an example.
 Here you can see I have a variable and I have assigned it the value 4.
 Apart from that we are checking the condition that if n is not equal to 4 then we can print
 n is not 4, right?
 But here as you can see n is 4.
 Therefore this if construct will not get evaluated.
 Now one important point that you must have to note down is that this printf function
 is actually the part of this if construct.
 Please note down.
 Why?
 Whenever we have single statement written immediately after the if construct or else
 construct then it is always considered to be the part of that if construct or else construct
 only, okay?
 Here immediately after this if construct you have a printf function which is just a single
 statement therefore it is considered to be the part of this if construct only, okay?
 Now what is the output of this particular program?
 The output is no output, right?
 Let's consider one more example.
 Here there is very minimal difference between these two examples.
 This example is equivalent to the example 1 but we have an else part as well.
 Here we are trying to print n is 4.
 The output is n is 4 because the condition itself is not satisfied therefore the else
 part will get executed and it will print the statement n is 4, right?
 As you can clearly see it is not necessary to put else part if we didn't find the need
 to inform the user that n is 4.
 If we find the need to inform the user that n is 4 then we have to put the else part here,
 right?
 Let's consider one more question.
 What is the difference between the following two examples?
 In this example we are checking whether n is equal to 4 or not and here also we are
 checking n is equal to 4 or not.
 Both are one and the same.
 If we talk about the difference between these two examples then there is no difference.
 Please note down.
 There is no difference between these two examples.
 Here you are putting curly braces and here you are not putting curly braces.
 Now you might ask me this question then why curly braces?
 If it is really not necessary to put curly braces then why do I need to put curly braces?
 Let's consider one example.
 Here in this example as you can clearly see I have declared a variable n and I have assigned
 it to value 5.
 After that you can see there is an if construct and this printf is part of this if construct
 as we know whenever we have a statement written immediately after the if construct then that
 statement is always the part of that if construct only.
 So this printf function is part of this if construct only.
 Now as n is not equal to 4 therefore this printf function will not get evaluated but
 n plus plus will get evaluated because n plus plus is not part of this if construct.
 Therefore the value of n is incremented to 6 and after that the value will get printed.
 So the output is 6.
 Let's consider one more example.
 Here in this example we are putting curly braces immediately after this if construct
 so that we would be able to include printf function as well as this n plus plus.
 Now if this condition is not satisfied then the n plus plus will not get evaluated therefore
 the value of n will not get incremented.
 As n is not equal to 4 therefore the value of n will not get incremented and as the output
 is 5.
 So we can clearly see that why it is necessary to put curly braces when we want to include
 two or more statements inside the if construct.
 If we just want to include a single statement immediately after the if construct then there
 is no requirement of putting curly braces but if we want to include more than one statement
 then we have to put curly braces.
 That is what we need to understand about the curly braces.
 Okay?
 Okay friends this is it for now.
 Thank you for watching this lecture.'''


if __name__ == "__main__":

    # llm = GemmaLLM_Api_EndPoint()
    # runtime = "cuda" if torch.cuda.is_available() else "cpu"
    # embed_model = embedding_model(runtime=runtime) 

    # chat_history = []

    # while True:
    #     print("\n\n")
    #     question = input("Enter Question: ")

    #     if question.lower() == "none": break
         
    #     result , chat_history , vecter_db = Chatbot(llm=llm, embedding_model=embed_model, question=question,
    #                                                 context=context, chat_history=chat_history
    #             )
    #     print()
    #     print(result["answer"])
    #     print()
    #     print(result)

    
    # print(summarizer(context))
    llm = Llm_EndPoint()
    
    model , tokenizer = load_generation_generation_model()
  
    
    outputs = question_generation_query(model, tokenizer, context, [0,1,2], 2000, 1000) 
    print(outputs)