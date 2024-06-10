from myqueue  import MyQueue


        def test_queue_size():
        queue1 = MyQueue()
        queue1.put(1, "condition")
        queue1.put(2, "proclaim")
        queue1.put(3, "claim")
        print(queue1.queue)
        assert(queue1.queue_size() is 3)

    def test_is_empty(self):
        queue1 = MyQueue()
        queue1.put(1, "condition")
        assert(queue1.is_empty() is True)

    def test_add(self):
        assert False

    def test_remove(self):
        assert False

    def test_put(self):
        assert False

    def test_delete_by_index(self):
        assert False

