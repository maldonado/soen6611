# importing the file that contains the data into variable bugfix_distribution
bugfix_distribution <- read.csv("~/git/chromium_explorer/bugfix_distribution.csv", header=TRUE)

#total number of open bugs in the system 
#proof of concept
r1_reported <- bugfix_distribution[1,2]
r1_fixed <- bugfix_distribution[1,3]
r1_remaining <- r1_reported - r1_fixed
r1_remaining

r2_reported <- bugfix_distribution[2,2]
r2_fixed <- bugfix_distribution[2,4]
r2_past_fixed <- bugfix_distribution[1,4]
r2_remaining <- r2_reported + r1_remaining - r2_fixed - r2_past_fixed
r2_remaining

r3_reported <- bugfix_distribution[3,2]
r3_fixed <- bugfix_distribution[3,5]
r3_past_fixed <- bugfix_distribution[1,5] + bugfix_distribution[2,5] 
r3_remaining <- r3_reported + r2_remaining - r3_fixed - r3_past_fixed
r3_remaining

#total number of open bugs in the system 
#script
for (i in 1:40) {
    past_fixed_temp <- 0L
    
    reported_name <- paste("r", i, "_reported",  sep = "")
    fixed_name <- paste("r", i, "_fixed",  sep = "")
    remaining_name <- paste("r", i, "_remaining",  sep = "")

    
    if(i != 1) {
        for (j in i:1) {
            past_fixed_temp <-  past_fixed_temp + bugfix_distribution[j,2+i]
        }
        assign(reported_name, bugfix_distribution[i,2])
        assign(fixed_name,  past_fixed_temp )
        assign(remaining_name, get(reported_name) - get(fixed_name) + get(paste("r", i -1, "_remaining",  sep = "")))
        print(paste(i, get(remaining_name), sep = " : " ))
    }
    else {
       assign(reported_name, bugfix_distribution[i,2])
       assign(fixed_name, bugfix_distribution[i,2+i] + past_fixed_temp)
       assign(remaining_name, get(reported_name) - get(fixed_name) )
       print(paste(i, get(remaining_name), sep = " : " ))
    }       
}