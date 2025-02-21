/**
 * @param {string} s
 * @return {boolean}
 */

class Stack {
    constructor(startingPile=[]){
        this.pile = startingPile;
    }
    pop() {
        return this.pile.pop()
    }
    push(el){
        this.pile.push(el)
    }
    peek(){
        console.log(this.pile)
    }
    pull(){
        return this.pile
    }
}
var isValid = function(s) {

        if (s.length <= 1) return false

        const closerMap = {'[':']','{':'}','(':')'};
        const stack = new Stack();

        for (let i = 0; i < s.length; i++) {
            let char = s[i];
            if (!!closerMap[char]) {
                stack.push(closerMap[char]);
            } else {
                let toMatch = stack.pop();
                if (toMatch != char) return false
            }
        }
        return stack.pull().length == 0
};

