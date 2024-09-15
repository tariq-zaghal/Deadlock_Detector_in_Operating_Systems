import pandas as pd
import numpy as np


def check_dimensions(allocation_file, request_file, available_file):
    return allocation_file.shape == request_file.shape and available_file.shape[1] == allocation_file.shape[1]


def detect_deadlock(allocation_file, request_file, available_file, status_list):
    execution_series = []
    deadlocked_processes = []
    is_deadlocked = False

    while not is_deadlocked:
        is_deadlocked = True
        for i in range(allocation_file.shape[0]):
            if compare_request_with_available(request_file.loc[i], available_file.loc[0]) and not status_list[i]:
                is_deadlocked = False
                update_available_list(allocation_file.loc[i], request_file.loc[i], available_file.loc[0])
                execution_series.append(allocation_file.loc[i].iat[0])
                status_list[i] = True

        if check_if_complete(status_list):
            return [True, execution_series]

    for i in range(allocation_file.shape[0]):
        if not status_list[i]:
            deadlocked_processes.append(allocation_file.loc[i].iat[0])
    return [False, deadlocked_processes]

def compare_request_with_available(request, available_vector):
    for i in range(len(available_vector)):
        if request.iat[i + 1] > available_vector.iat[i]:
            return False
    return True

def update_available_list(allocated_vector, request_vector, available_vector):
    for i in range(len(available_vector)):
        available_vector.iat[i] = available_vector.iat[i] + allocated_vector.iat[i + 1]


def check_if_complete(status_list):
    for i in range(len(status_list)):
        if not status_list[i]:
            return False
    return True
