#R language have three types 
#numeric(number),logical(true and false),character(string)
# "=" is behalf of "<-"
a = 1 + 2
#numeric
a <- 110
A <- 10
#logical
mylogical <- True
mylogical <- F
#character
mycharacter <- "my little story"
#factor https://swcarpentry.github.io/r-novice-inflammation/12-supp-factors/index.html
#Factors are used to represent categorical data. 
#Factors can be ordered or unordered and are an important class for statistical analysis and for plotting.  
myfactor <- as.factor("female")
#vector
vec1 <- c(1,2,2,3,23,0.2)
vec2 <- c(T,F,False,True,F,T)
vec3 <- c("a","b","b","my little story",z,20)
vec4 <- as.factor(c("female","male","male"))
#list can contain different kinds of type in R programming.
mylist <- list(vec1,vec2,vec3,20,list(vec1,vec2),mean)
#data frame : LIKE A TABLE,we need the same row and column
df = data.frame(vec1,vec2)
#matrices
mymatrices <- matrix (vec3,2,3)
#indexing 索引,2 is the second,not the third 
vec2[2]
vec3[1:6]
vec3[1:4]
vec3[-1] #all the value,except the first one
#function 
new_sum <- function (value1,value2){
    results <- value1 + value2
    return (results)
}
new_sum(10,20)
new_division(10,)