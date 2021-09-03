# python3
# Author: Junzhong Loo
# Date: 2/9/2021

from collections import namedtuple, deque
from typing import Deque
# from queue import Queue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        processor_queue = self.finish_time

        # pop from front of processor_queue, all packets that have been processed
        arrived_time = request.arrived_at
        while arrived_time > 0 and len(processor_queue) > 0:
            finish_time_of_next_job = processor_queue.popleft()
            arrived_time -= finish_time_of_next_job
            # next job in queue not finished processing, pop back into queue
            if arrived_time < 0:
                processor_queue.appendleft(finish_time_of_next_job)

        # first packet
        if len(processor_queue) == 0:
            # append to queue if processing time more than 0
            if request.time_to_process > 0:
                processor_queue.append(
                    request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)

        # if buffer is full, drop packet
        if ((self.size - len(processor_queue)) < 1):
            return Response(True, -1)
        else:
            # find finish time for new packet and add to finish_time
            last_job_finish_time = processor_queue.pop()
            new_packet_finish_time = last_job_finish_time + request.time_to_process
            processor_queue.extend(
                [last_job_finish_time, new_packet_finish_time])
        new_packet_start_time = last_job_finish_time
        return Response(False, new_packet_start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()


""" 
sample 4
buffer size | n_requests
1               2
arrived at | time to process        was_dropped | started at
0               1                       False       0
1               1                       False       1


1) pop from front of finish_time the packets that are already processed
by time of arrive of new packet
    finish_time[0] - 1
    if finish_time[0] === 0
        finish_time.pop(0)
2) add the finish time for the new packet to the finish time

3) if buffer is full, drop packet, else add time to process to finish time
    if finish_time.length == self.size
        return Response(True, -1)
    else:
        finish_time.append(response.time_to_process)
"""
