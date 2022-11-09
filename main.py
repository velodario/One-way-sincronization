import source_f, replica_f, os, logging

def log_operation(log_file):
    logging.basicConfig(filename=log_file,
                    format='%(asctime)s %(message)s',
                    filemode='w')

if __name__ == '__main__':
    s = source_f.Source()
    r = replica_f.Replica()

    log_file = input("Insert log file name: ")

    log_operation(log_file)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if s.check_path() and r.check_path():
        logging.info("source and replica folders exist")
        if os.listdir(s.source_path) == []:
            logging.warning("No files found in the source directory. Deleting replica files")
            r.delete_files()
        else:
            names = s.read_files()
            r.write_files(names)
            logging.info("all files copied to replica folder")
    else:
        logging.error("source or replica folder does not exist")      

