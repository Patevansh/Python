from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty."

    def display(self):
        return list(reversed(self.stack)) 

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)

    def front(self):
        return self.queue[0] if self.queue else "Queue is empty."

    def display(self):
        return self.queue

stack = Stack()
queue = Queue()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stack", methods=["POST"])
def stack_operations():
    data = request.json
    action = data.get("action")
    item = data.get("item")

    if action == "push":
        stack.push(item)
    elif action == "pop":
        stack.pop()
    elif action == "peek":
        return jsonify(message=stack.peek(), stack=stack.display())

    return jsonify(stack=stack.display())

@app.route("/queue", methods=["POST"])
def queue_operations():
    data = request.json
    action = data.get("action")
    item = data.get("item")

    if action == "enqueue":
        queue.enqueue(item)
    elif action == "dequeue":
        queue.dequeue()
    elif action == "front":
        return jsonify(message=queue.front(), queue=queue.display())

    return jsonify(queue=queue.display())

if __name__ == "__main__":
    app.run(debug=True)
