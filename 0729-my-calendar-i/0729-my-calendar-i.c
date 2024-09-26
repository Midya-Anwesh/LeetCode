typedef struct date{
    int booked_date[2];
    struct date *before;
    struct date *after;
} MyCalendar;


MyCalendar* myCalendarCreate() {
    return calloc(sizeof(MyCalendar), 1);
}

bool isRoot(MyCalendar *obj){
    if (obj->booked_date[1] <= 0){
        return true;
    }
    return false;
}

bool overlap(MyCalendar *obj, int start, int end){
    if ( (start < obj->booked_date[0] && end <= obj->booked_date[0]) || \
    (start >= obj->booked_date[1] && end >= obj->booked_date[1])){
        return false;
    }
    return true;
}

void bookDate(MyCalendar *obj, int start, int end){
    obj->booked_date[0] = start;
    obj->booked_date[1] = end;
    obj->before = NULL;
    obj->after = NULL;
}

bool myCalendarBook(MyCalendar* obj, int start, int end) {
    if (isRoot(obj)){
        obj->booked_date[0] = start;
        obj->booked_date[1] = end;
        return true;
    }
    while (!overlap(obj, start, end)){
        if (start < obj->booked_date[0]){
            if (obj->before == NULL){
                obj->before = malloc(sizeof(MyCalendar));
                bookDate(obj->before, start, end);
                return true;
            }
            obj = obj->before;
        }
        else if (start >= obj->booked_date[1]){
            if (obj->after == NULL){
                obj->after = malloc(sizeof(MyCalendar));
                bookDate(obj->after, start, end);
                return true;
            }
            obj = obj->after;
        }
    }
    return false;
}

void myCalendarFree(MyCalendar* obj) {
    if (obj == NULL){
        return;
    }
    myCalendarFree(obj->before);
    myCalendarFree(obj->after);
    free(obj);
}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, start, end);
 
 * myCalendarFree(obj);
*/