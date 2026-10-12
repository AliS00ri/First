fun main(){
    print ("chose rock or paper or scissors :")
    val player = readln().lowercase ()
if (player =="rock")
    println("u chose : rock")
else if (player =="paper")
    println("u chose : paper")
else if (player =="scissors")
    println("u chose : scissors")
else
    println("ERROR")

val pc =listOf("paper","scissors","rock").random().lowecase()
println("pc chose : $pc")
println("..............")
println("..............")
if (pc==player)
    println("its a tie")
else if (player == "rock" && pc =="paper"){
    println("y lose")
}
else if (player == "rock" && pc =="scissors"){
    println("y Win")
}


else if (player == "scissors" && pc =="paper"){
    println("y Win")
}
else if (player == "scissors" && pc =="paper"){
    println("y Win")
}


else if (player == "scissors" && pc =="rock"){
    println("y lose")
}
else if (player == "scissors" && pc =="paper"){
    println("y Win")
}
}
