library(ggplot2)
library(ggthemes)

# Classic Theme
ggplot(...,aes(x= ...)) +  
  geom_bar(...(fill= ...)) +
  theme_classic()

# BW Theme

ggplot(...,aes(x= ...)) +  
  geom_bar(...(fill= ...)) +
  theme_bw()

# Graph 객체 ...

# Other Theme
Graph + theme_bw() + ggtitle("Theme_bw") 
Graph + theme_classic() + ggtitle("Theme_classic") 
Graph + theme_dark() + ggtitle("Theme_dark") 
Graph + theme_light() + ggtitle("Theme_light")  
Graph + theme_linedraw() + ggtitle("Theme_linedraw") 
Graph + theme_minimal() + ggtitle("Theme_minimal") 
Graph + theme_test() + ggtitle("Theme_test") 
Graph + theme_void() + ggtitle("Theme_vold") 
