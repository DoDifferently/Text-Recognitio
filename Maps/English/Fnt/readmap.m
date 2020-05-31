function [NUMclass,NUMclass,NUMimg,classname,fontname,fontweight,fontangle]=readmap
  [NUMclass,NUMclass,NUMimg,classname,fontname,fontweight,fontangle]=textread('map.txt','Sample%d/img%d-%d;%c;%s;%s;%s','whitespace',';');
end