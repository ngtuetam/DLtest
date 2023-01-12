function isPositive(a) {
    
    try {
        if(a>0){
           return "YES";
        }
        else if(a<0){
            throw new Error('Negative Error');
          }
         else{
            throw new Error('Zero Error');
        }       
        }
        catch(err) {
            return err.message;
        }
}