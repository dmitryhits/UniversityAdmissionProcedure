# write your code here
#total = 0
#n_applicants = int(input())

def sort(non_sorted, indexes):
    if non_sorted and len(indexes) == 2:
        i1 = indexes[0]
        i2 = indexes[1]
        return sorted(non_sorted,
                      key=lambda x: (-max((float(x[2 + i1]) + float(x[2 + i2])) / 2, float(x[6])), x[0] + x[1]))
    elif non_sorted and len(indexes) == 1:
        i1 = indexes[0]
        return sorted(non_sorted, key=lambda x: (-max(float(x[2 + i1]), float(x[6])), x[0] + x[1]))
    else:
        return non_sorted


def i_exam(dep):
    exams = ['physics', 'chemistry', 'math', 'computer science']
    department_exams = {'Biotech': ['chemistry', 'physics'],
                        'Chemistry': ['chemistry'],
                        'Engineering': ['computer science', 'math'],
                        'Mathematics': ['math'],
                        'Physics': ['physics', 'math']}

    indexes = [exams.index(exam) for exam in department_exams[dep]]
    return indexes


department_names = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
exams = ['physics', 'chemistry', 'math', 'computer science']

choices = [1, 2, 3]
departments_by_choice = {choice: {dep: [] for dep in department_names} for choice in choices}
accepted_applicants = {d: [] for d in department_names}
remaining_applicants = []
m_places = int(input())

# with open('/Users/hits/Downloads/applicant_list.txt') as applicant_file:
with open('applicants.txt') as applicant_file:
    for applicant in applicant_file:
        applicant = applicant.split()
        remaining_applicants.append(applicant)


for choice in choices:
    for applicant in remaining_applicants:
        departments_by_choice[choice][applicant[choice + 6]].append(applicant)

    remaining_applicants.clear()
    for department, applicants in departments_by_choice[choice].items():
        i = i_exam(department)
        sorted_applicants = sort(applicants, i)
        remaining = m_places - len(accepted_applicants[department])
        accepted_applicants[department].extend(sorted_applicants[:remaining])
        remaining_applicants.extend(sorted_applicants[remaining:])


for dep, applicants in accepted_applicants.items():
    print(dep)
    with open(f'{dep}.txt', 'w') as f:
        i = i_exam(dep)
        for applicant in sort(applicants, i):
            if len(i) == 2:
                i1 = i[0]
                i2 = i[1]
                print(applicant[0], applicant[1], max((float(applicant[2 + i1]) + float(applicant[2 + i2])) / 2, float(applicant[6])))
                f.write(f'{applicant[0]} {applicant[1]} {max((float(applicant[2 + i1]) + float(applicant[2 + i2])) / 2, float(applicant[6]))}\n')
            else:
                i1 = i[0]
                print(applicant[0], applicant[1], max(float(applicant[2 + i1]), float(applicant[6])))
                f.write(f'{applicant[0]} {applicant[1]} {max(float(applicant[2 + i1]), float(applicant[6]))}\n')
        print()

# mean_score = total / 3
# print(mean_score)
# if mean_score >= 60:
#     print('Congratulations, you are accepted!')
# else:
#     print('We regret to inform you that we will not be able to offer you admission.')
