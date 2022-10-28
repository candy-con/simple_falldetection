#Receives (x,y) from data frame and draws the coordinates on the pose estimation output video.
cv2.circle(canvas, (x, y), 3, color, -1)                                                         
                  cv2.putText(canvas,"("+str(x)+","+str(y)+")",(int(x), int(y)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                  fontScale=1,
                  color=(0, 255, 0),
                  thickness=1)
                  cur_df = 0 #holds current size of df 
                  count = 1 #if count is over 2, comparison starts 
                  a = 1
                  curr_state = "Normal"
                  prev_state = curr_state                   
                  for k in range(len(df)):
                    if k >= 1:
                        if count == 1:
                          cur_df = len(df.columns)
                          count += 1
                        elif count >1:
                            dif_df = len(df.columns) - cur_df 
                            if dif_df >= 0:
                              if (df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) <0: 
                                if abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) <= 20:
                                  if prev_state == "Normal" and curr_state == "Normal":
                      
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0), #red = normal state 
                                    thickness = 4)

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df

                                    curr_state = "Normal"
#If previous state was fall and the next state is Normal, it will transcribe the state to Fall
                                  elif prev_state == "Fall" and curr_state == "Normal":
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0), #red = normal state 
                                    thickness = 4)

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df

                                    curr_state = "Fall"

#If previous state was recovering and the next state is the same, it will maintain the state                  
                                elif 50 > abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 20:
                                  if prev_state == "Recovering" and curr_state == "Recovering":
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Recovering",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green = recovering state 
                                    thickness = 4)

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df
                                  
                                    curr_state = "Recovering"

                                  if prev_state == "Normal" and curr_state == "Recovering":
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0), # red = normal state 
                                    thickness = 4)
                                    
                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df
                                  
                                    curr_state = "Normal"


                              elif (df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 0: #Fall 
                                if abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) <= 20:

                                  if prev_state == "Normal" and curr_state == "Normal":
                      
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0), #red = normal state 
                                    thickness = 4)

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df

                                    curr_state = "Normal"

                                  elif prev_state == "Fall" and curr_state == "Normal":
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(255, 0, 0), #red = normal state 
                                    thickness = 4)

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                    thickness = -1)

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df

                                    curr_state = "Fall"

          

                                elif 50 > abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 20:
                                  cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                  thickness = -1)

                                  cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                  fontScale=1,
                                  color=(0, 0, 255), #blue = fall state 
                                  thickness = 4) 

                                  cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255),
                                  thickness = -1) 

                                  cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                  fontScale=1,
                                  color=(0, 255, 0), #green, to check prev and current two y values
                                  thickness = 4)

                                  cur_df = len(df.columns)
                                  a += dif_df

                                  curr_state = "Fall"

                              if dif_df < 0:
                                if (df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) < 0:
                                  if abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) <= 20:
                                     if prev_state == "Normal" and curr_state == "Normal":
                      
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(255, 0, 0), #red = normal state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Normal"

                                     elif prev_state == "Fall" and curr_state == "Normal":
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(255, 0, 0), #red = normal state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Fall"


                                  elif 50 > abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 20:
                                    if prev_state == "Recovering" and curr_state == "Recovering":
                                    
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Recovering",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green = recovering state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Recovering"
#IF the previous state was Normal and the next state is Recovering, it will transcribe the state to Normal
                                    elif prev_state == "Normal" and curr_state == "Recovering":
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(255, 0, 0), #red = normal state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Normal"

                                elif (df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 0:
                                  if abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) <= 20:
                                    #start
                                    if prev_state == "Normal" and curr_state == "Normal":
                      
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Normal",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(255, 0, 0), #red = normal state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Normal"

                                    elif prev_state == "Fall" and curr_state == "Normal":
                                      cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                      thickness = -1)

                                      cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(255, 0, 0), #red = normal state 
                                      thickness = 4)

                                      cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255), 
                                      thickness = -1)

                                      cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=1,
                                      color=(0, 255, 0), #green, to check prev and current two y values
                                      thickness = 4)

                                      cur_df = len(df.columns)
                                      a += dif_df

                                      curr_state = "Fall"

                                  elif 50 > abs(df.iloc[k,a+dif_df] - df.iloc[k-1,a+dif_df]) > 20:
                                    cv2.rectangle(canvas,pt1=(25,25),pt2=(220,75),color=(255,255,255),
                                    thickness = -1)

                                    cv2.putText(canvas,"Fall",(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 0, 255), #blue = fall state 
                                    thickness = 4) 

                                    cv2.rectangle(canvas,pt1=(220,25),pt2=(500,75),color=(255,255,255),
                                    thickness = -1) 

                                    cv2.putText(canvas,"("+str(df.iloc[k,a+dif_df])+","+str(df.iloc[k-1,a+dif_df])+")",(250,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1,
                                    color=(0, 255, 0), #green, to check prev and current two y values
                                    thickness = 4)

                                    cur_df = len(df.columns)
                                    a += dif_df

                                    curr_state = "Fall"                              
