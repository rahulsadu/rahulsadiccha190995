def email_fetch(data ,filename_write):
    emails=[]
    for line in data:
        for word in line.split():
            if '@' in word:
                emails.append(word)
    status=write_email(emails,filename_write)
    return status

def write_email(e,name):
    fp=open(name,'w')
    fp.writelines(e)
    return True


def main():
    filename_read='product.txt'
    filename_write='emails.txt'
    fp=open(filename_read)
    data=fp.readlines()
    email_fetch(data ,filename_write)
    st=email_fetch(data,filename_write)
    if st:
        print("operation successfully performed")
    else:
        print("failed")

    if __name__=='__main__':
        main()