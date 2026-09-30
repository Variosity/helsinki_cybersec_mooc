#!/usr/bin/env python3
import sys
import sqlite3


def read_database(conn):
	agents = []
	cursor = conn.cursor()
	cursor.execute('SELECT id, name FROM Agent ORDER BY id')
	agents = cursor.fetchall()
	return agents



def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	agents = read_database(conn)
	for agent in agents:
		print(agent[0], agent[1])

if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
