# importing the file that contains the data into variable bugfix_distribution
bugfix_distribution <- read.csv("~/git/chromium_explorer/bugfix_distribution.csv", header=TRUE)

#loop creating new variables for each row in the file, load the values in oercentage, create a bar plot in the home directory
for(i in 1:41) { 
    variable_name <- paste("r", i,  sep = "")
    pdf(paste(variable_name, "pdf", sep = "."))
    barplot(assign(variable_name, as.matrix(bugfix_distribution[i,3:41]/bugfix_distribution[i,2])))
    dev.off()
};

#Get all the values in memory and sum them:
#the current release + current release + 1 for bugs 
#the third release forward for defect debt
for(i in 1:37) {
    in_memory_var <- paste("r", i,  sep = "")
    temp_var <- get(in_memory_var)
    ddebt_variable_name <- paste(in_memory_var, "defect_debt_sum", sep = "_")
    bugs_variable_name <- paste(in_memory_var, "bug_sum", sep = "_")
    assign(ddebt_variable_name, sum(temp_var[1,(i+2):39]))
    assign(bugs_variable_name, sum(temp_var[1,(i): (1+i)]))
};

#calculate the mean for defect debt
mean( r1_defect_debt_sum,  r2_defect_debt_sum,  r3_defect_debt_sum,  r4_defect_debt_sum,  r5_defect_debt_sum, r6_defect_debt_sum, 
      r7_defect_debt_sum,  r8_defect_debt_sum,  r9_defect_debt_sum, r10_defect_debt_sum, r11_defect_debt_sum, r12_defect_debt_sum,
     r13_defect_debt_sum, r13_defect_debt_sum, r14_defect_debt_sum, r15_defect_debt_sum, r16_defect_debt_sum, r17_defect_debt_sum,
     r18_defect_debt_sum, r19_defect_debt_sum, r20_defect_debt_sum, r21_defect_debt_sum, r22_defect_debt_sum, r23_defect_debt_sum, 
     r24_defect_debt_sum, r25_defect_debt_sum, r26_defect_debt_sum, r27_defect_debt_sum, r28_defect_debt_sum, r29_defect_debt_sum, 
     r30_defect_debt_sum, r31_defect_debt_sum, r32_defect_debt_sum, r33_defect_debt_sum, r34_defect_debt_sum, r35_defect_debt_sum, 
     r36_defect_debt_sum, r37_defect_debt_sum, r38_defect_debt_sum, r39_defect_debt_sum, r40_defect_debt_sum, r41_defect_debt_sum)

#calculate the mean for bugs
mean( r1_bug_sum,  r2_bug_sum,  r3_bug_sum,  r4_bug_sum,  r5_bug_sum, r6_bug_sum, 
      r7_bug_sum,  r8_bug_sum,  r9_bug_sum, r10_bug_sum, r11_bug_sum, r12_bug_sum,
     r13_bug_sum, r13_bug_sum, r14_bug_sum, r15_bug_sum, r16_bug_sum, r17_bug_sum,
     r18_bug_sum, r19_bug_sum, r20_bug_sum, r21_bug_sum, r22_bug_sum, r23_bug_sum, 
     r24_bug_sum, r25_bug_sum, r26_bug_sum, r27_bug_sum, r28_bug_sum, r29_bug_sum, 
     r30_bug_sum, r31_bug_sum, r32_bug_sum, r33_bug_sum, r34_bug_sum, r35_bug_sum, 
     r36_bug_sum, r37_bug_sum, r38_bug_sum, r39_bug_sum, r40_bug_sum, r41_bug_sum)

